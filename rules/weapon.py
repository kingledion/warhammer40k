from typing import Any


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
        name: str,
        range: int,
        a: int,
        ws: int,
        s: int,
        ap: int,
        d: int,
        abilities: list[WeaponAbility] = []
    ):
        self.name: str = name
        self.range: int = range
        self.a: int = a
        self.ws: int = ws
        self.s: int = s
        self.ap: int = ap
        self.d: int = d
        
        self.abilities: list[WeaponAbility] = abilities

    def __str__(self) -> str:
        return self.name
    
    def get_range(self) -> int:
        return self.range
        
    def get_attacks(self) -> int:
        return self.a
    
    def get_score(self) -> int:
        return self.ws
    
    def get_strength(self) -> int:
        return self.s
    
    def get_armor_pierce(self) -> int:
        return self.ap
    
    def get_damage(self) -> int:
        return self.d
    
    def is_assault(self) -> bool:
        return Assault in self.abilities
    
    def is_heavy(self) -> bool:
        return Heavy in self.abilities
    
    def is_pistol(self) -> bool:
        return Pistol in self.abilities
    
