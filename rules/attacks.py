import numpy as np
import numpy.typing as npt
#from typing import Self  **** UPGRATE TO 3.11 *****

from rules.weapon import Weapon
from rules.unit import Unit
from rules.rolls import d6
from rules.util import limit_1

class Attack:
    def __init__(self, 
                 weapon: Weapon, 
                 n: int, 
                 rng: int, 
                 target: Unit, 
                 stationary: bool = False):
        self.weapon: Weapon = weapon
        self.n: int = n
        self.rng: int = rng
        self.target: Unit = target
        self.stationary: bool = stationary


class AttackResult:
    def __init__(self, hits: npt.NDArray, crit_hits: npt.NDArray):
        self.hits: npt.NDArray = hits
        self.crit_hits: npt.NDArray = crit_hits

    def with_wounds(self, wnds: npt.NDArray, crit_wnds: npt.NDArray):
        self.wnds: npt.NDArray = wnds
        self.crit_wnds: npt.NDArray = crit_wnds
        return self
    
    def with_saves(self, wnds_not_saved: npt.NDArray, mortal_wnds: npt.NDArray):
        self.wnds_not_saved: npt.NDArray = wnds_not_saved
        self.mortal_wnds: npt.NDArray = mortal_wnds
        return self

def hit(attk: Attack) -> AttackResult:

    atks = attk.weapon.get_attacks()
    # if it is d something, calcualte

    # modify atks by range for rapid fire
    rapid_fire = attk.weapon.has_rapid_fire()
    if rapid_fire and attk.rng <= attk.weapon.get_range() / 2:
        atks += rapid_fire

    # torrent always hits, can't crit
    if attk.weapon.has_torrent():
        return np.full(attk.n*atks, 1)

    # determine roll needed to hit
    to_hit = attk.weapon.get_score()

    # determine roll needed to crit
    to_crit = 6

    # get hit adjustment, if applicable
    adj = 0
    # if heavy, add one when remaining stationary
    if attk.stationary and attk.weapon.is_heavy():
        adj = adj + 1
    # max adj range (-1, 1)
    adj = limit_1(adj)

    # create hit rolls 
    rolls = d6(attk.n * atks)

    # determine crits
    crits = (rolls >= to_crit)

    # determine hits including crits
    may_hit = np.where(rolls > 1, rolls, 0)
    hits = (may_hit + adj >= to_hit | crits)

    # if sustained hits, crits cause additional hits
    sustained_hits = attk.weapon.has_sustained_hits()
    if sustained_hits > 0:
        hits = hits + crits * sustained_hits

    return AttackResult(hits.astype(int), crits.astype(int))
    

def wound(rslt: AttackResult, attk: Attack) -> AttackResult:

    # if there are no hits, there are no wounds
    if max(rslt.hits) == 0:
        l = rslt.hits.shape
        return rslt.with_wounds(np.zeros(l), np.zeros(l))

    # if lethal hits, do not roll for crit hits (wounds are added later)
    if attk.weapon.has_lethal_hits():
        hits = rslt.hits - rslt.crit_hits
    else:
        hits = rslt.hits 

    # make a 2d array out of hits
    wnd_hits = np.vstack([(hits > i).astype(int) for i in range(max(hits))])

    s = attk.weapon.get_strength()
    t = attk.target.get_target().get_toughness()

    # determine roll needed to wound
    to_wound = 6
    if s >= t * 2:
        to_wound = 2
    elif s > t:
        to_wound = 3
    elif s == t:
        to_wound = 4
    elif s > t/2:
        to_wound = 5

    # determine roll needed to crit
    to_crit = 6
    # if anti-x applies, adjust crit roll
    keyword, val = attk.weapon.has_anti_x()
    if keyword and attk.target.get_target().has_keyword(keyword):
        to_crit = val

    # get wound adjustment, if applicable
    adj = 0
    # max adj range (-1, 1)
    adj = limit_1(adj)

    # roll for wounds 
    rolls = d6(wnd_hits.shape) * wnd_hits
    # determine crits
    crits = rolls >= to_crit

    # determine wounds including crits
    may_wnd = np.where(rolls > 1, rolls, 0)
    wnds = may_wnd + adj >= to_wound | crits

    # if twin-linked, reroll all hits that didn't crit
    if attk.weapon.has_twin_linked():
        re_rolls = d6(wnd_hits.shape) * (wnd_hits - crits)
        crits = crits | re_rolls >= to_crit
        may_wnd = np.where(re_rolls > 1, re_rolls, 0)
        wnds = wnds | may_wnd + adj >= to_wound | crits

    # convert from 2d matrix to counts
    wnds_sum = np.sum(wnds, axis=0)
    crits_sum = np.sum(crits, axis=0)

    # add wounds for lethal_hits
    if attk.weapon.has_lethal_hits():
        wnds_sum = wnds_sum + rslt.crit_hits

    return rslt.with_wounds(wnds_sum.astype(int), crits_sum.astype(int))


def save(rslt: AttackResult, attk: Attack) -> AttackResult:

    # if devastating wounds, add mortal wound damage, remove crits from wnds
    if attk.weapon.has_devastating_wounds():
        mortal = rslt.crit_wnds
        wnds = rslt.wnds - rslt.crit_wnds
    else:
        mortal = np.zeros(rslt.crit_wnds.shape, dtype=int)
        wnds = rslt.wnds

    # make a 2d array out of wounds
    if max(wnds) >= 1:
        dmg_wnds = np.vstack([(wnds > i).astype(int) for i in range(max(wnds))])
    else:
        return rslt.with_saves(np.zeros(wnds.shape, dtype=int), mortal)

    # calculate the save to use
    ap = attk.weapon.get_armor_pierce()
    sv = attk.target.get_target().get_save()
    invul = attk.target.get_target().get_invulnerable()
    save = min(sv - ap, invul) if invul else sv - ap

    # roll for wound saves
    rolls = d6(dmg_wnds.shape) * dmg_wnds
    wounds_not_saved = np.sum((rolls != 0) & (rolls < save) | (rolls == 1), axis=0)

    return rslt.with_saves(wounds_not_saved.astype(int), mortal.astype(int))


DamageResult = np.ndarray
# class DamageResult:
#     def __init__(self, damage: npt.NDArray, mortal_damage: npt.NDArray) -> Self:
#         self.damage: npt.NDArray = damage
#         self.mortal_damage: npt.NDArray = mortal_damage

def damage(rslt: AttackResult, attk: Attack) -> DamageResult:

    # determine weapon damage
    dmg = attk.weapon.get_damage()
    # if it is d-something, make func for calculating damages
    dmg_func = lambda x: x * dmg

    # determine damage dealt
    damage = np.sum(dmg_func(rslt.wnds_not_saved), axis=0)

    # determine mortal wound damage
    mortal = np.sum(dmg_func(rslt.mortal_wnds), axis=0)

    # count dammage and adjudicate feel no pain as you go ...

    return damage + mortal
