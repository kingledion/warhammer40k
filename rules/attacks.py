from rules.weapon import Weapon
from rules.unit import Unit
from rules.rolls import d6

class HitResult:
    def __init__(self, hits: int, crits: int):
        self.hits: int = hits
        self.crits: int = crits

    def __str__(self) -> str:
        return f'(hits: {self.hits}, crits: {self.crits})'

    def get_all_hits(self) -> int:
        return self.hits + self.crits
    
    def get_hits(self) -> int:
        return self.hits
    
    def get_crits(self) -> int:
        return self.crits

def hit(weapon: Weapon, cnt: int, _rng: int, _target: Unit, stationary: bool = False) -> HitResult:

    # modify atks by range for rapid fire
    atks = weapon.get_attacks()
    # torrent always hits

    rolls = d6(cnt * atks)
    crits = sum(x == 6 for x in rolls)
    may_hit = [x for x in rolls if x < 6 and x > 1]


    adj = 0
    if stationary and weapon.is_heavy():
        adj = adj + 1
    # max adj range (-1, 1)
    if adj > 1:
        adj = 1
    if adj < -1:
        adj = -1

    hits = sum(x + adj >= weapon.get_score() for x in may_hit)


    # if sustained hits, convert crits to extra hits

    return HitResult(hits, crits)

class WoundResult:
    def __init__(self, wounds: int, crits: int):
        self.wounds: int = wounds
        self.crits: int = crits

    def __str__(self) -> str:
        return f'(wounds: {self.wounds}, crits: {self.crits})'

    def get_all_wounds(self) -> int:
        return self.wounds + self.crits
    
    def get_wounds(self) -> int:
        return self.wounds
    
    def get_crits(self) -> int:
        return self.crits
    

def wound(weapon: Weapon, hits: HitResult, _rng: int, target: Unit) -> WoundResult:

    # if lethal hits, critical hits automatically wound
    wounds = 0
    have_hit = hits.get_all_hits()

    s = weapon.get_strength()
    t = target.get_target().get_toughness()

    to_wound = 6
    if s >= t * 2:
        to_wound = 2
    elif s > t:
        to_wound = 3
    elif s == t:
        to_wound = 4
    elif s > t/2:
        to_wound = 5

    rolls = d6(have_hit)
    # if anti applies, adjust critical value
    to_crit = 6

    crits = sum(x >= to_crit for x in rolls)
    may_wound = [x for x in rolls if x < to_crit and x > 1]

    adj = 0
    # max adj range (-1, 1)
    if adj > 1:
        adj = 1
    if adj < -1:
        adj = -1

    wounds = wounds + sum(x + adj >= to_wound and x < to_crit for x in may_wound)

    # if twin-linked, try again for may_wound - wound


    return WoundResult(wounds, crits)

DamageResult = int

def damage(weapon: Weapon, wounds: WoundResult, _range: int, target: Unit) -> DamageResult:

    # if devastating wounds, convert critical to mortal
    mortal = 0

    ap = weapon.get_armor_pierce()
    sv = target.get_target().get_save()
    invul = target.get_target().get_invulnerable()
    save = min(sv - ap, invul) if invul > 0 else sv - ap

    rolls = d6(wounds.get_all_wounds())
    wounds_not_saved = sum(x < save for x in rolls)

    dmg = weapon.get_damage()
    damage = wounds_not_saved * dmg + mortal

    fnp = target.get_target().get_feel_no_pain()
    if fnp > 0:
        rolls = d6(damage)
        return sum(x < fnp for x in rolls)
    else:
        return damage
