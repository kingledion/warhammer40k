from weapon import *
from tags import *

class UnitAbility:
    def __init__(self, name, val=0):
        self.name = name
        self.value = val

class Unit:

    def __init__(
        self,
        m: int,
        t: int,
        sv: int,
        w: int,
        ld: int,
        oc: int,
        tags: list[Tag] = [],
        weapons: list[Weapon] = [],
    ):
        self.m: int = m
        self.t: int = t
        self.sv: int = sv
        self.w: int = w
        self.ld: int = ld
        self.oc: int = oc

        self.tags: list[Tag] = tags
        self.weapons: list[Weapon] = weapons

    def get_toughness(self):
        return self.t
    


# Space Marines
IntercessorSquad = Unit(6, 4, 3, 2, 6, 2, tags = [adeptus_astartes, infantry], weapons = [BoltPistol, BoltRifle, CCW_Intercessor])

# Necrons
NecronWarrior = Unit(5, 4, 4, 1, 7, 2, tags = [necrons, infantry], weapons = [GaussFlayer, CCW_NecronWarrior])