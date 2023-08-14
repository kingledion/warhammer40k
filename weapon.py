class WeaponAbility:
    def __init__(self, name, val=0):
        self.name = name
        self.value = val


Assault = WeaponAbility("assault")
Heavy = WeaponAbility("heavy")
Pistol = WeaponAbility("pistol")

# assault=False,
# rapid_fire=0,
# # ignores_cover=False,
# twin_linked=False,
# pistol=False,
# torrent=False,
# lethal_hits=False,
# lance=False,
# # ignores_cover=False,
# # precision=False,
# blast=False,
# melta=0,
# heavy=False,
# hazardous=False,
# devastating_wounds=False,
# sustained_hits=0,
# extra_attacks=False, 
# anti_infantry=0,

class Weapon:

    def __init__(
        self,
        range: int,
        a: int,
        ws: int,
        s: int,
        ap: int,
        d: int,
        abilities: list[WeaponAbility]
    ):
        self.range: int = range
        self.a: int = a
        self.ws: int = ws
        self.s: int = s
        self.ap: int = ap
        self.d: int = d
        
        self.abilities: list[WeaponAbility] = abilities
    

    def get_score(self) -> int:
        return self.ws
    
    def get_strength(self) -> int:
        return self.s
    
    def get_armor_pierce(self) -> int:
        return self.ap
    
    def get_damage(self) -> int:
        return self.d
    
    def is_heavy(self) -> bool:
        return Heavy in self.abilities
    


# Space Marines
BoltPistol = Weapon(12, 1, 3, 4, 0, 1, [Pistol])
BoltRifle = Weapon(24, 2, 3, 4, -1, 1, [Assault, Heavy])
CCW_Intercessor = Weapon(0, 3, 3, 4, 0, 1)

# Necrons
GaussFlayer = Weapon(24, 1, 4, 4, 0, 1)
CCW_NecronWarrior = Weapon(0, 1, 4, 4, 0, 1)