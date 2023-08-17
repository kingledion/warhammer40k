from rules.keyword import Keyword
import rules.keyword


class WeaponAbility:
    def __init__(self, name: str, val: int = 0):
        self.name: str = name


Assault = WeaponAbility("Assault")
Heavy = WeaponAbility("Heavy")
Pistol = WeaponAbility("Pistol}")
RapidFire1 = WeaponAbility("Rapid Fire 1")
RapidFire2 = WeaponAbility("Rapid Fire 2")
Torrent = WeaponAbility("Torrent")
SustainedHits1 = WeaponAbility("Sustained Hits 1")
SustainedHits2 = WeaponAbility("Sustained Hits 2")
LethalHits = WeaponAbility("Lethal Hits")
AntiInfantry4 = WeaponAbility("Anti-Infantry 4+")
DevastatingWounds = WeaponAbility("Devastating Wounds")
TwinLinked = WeaponAbility("Twin Linked")


# # ignores_cover=False,
# lance=False,
# # ignores_cover=False,
# # precision=False,
# blast=False,
# melta=0,
# hazardous=False,
# extra_attacks=False, 

class Weapon:

    def __init__(
        self,
        name: str,
        range: int,
        a: int | str,
        ws: int,
        s: int,
        ap: int,
        d: int | str,
        abilities: set[WeaponAbility] = []
    ):
        self.name: str = name
        self.range: int = range
        self.a: int | str = a
        self.ws: int = ws
        self.s: int = s
        self.ap: int = ap
        self.d: int | str = d
        
        self.abilities: set[WeaponAbility] = abilities

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
    
    def has_assault(self) -> bool:
        return Assault in self.abilities
    
    def has_heavy(self) -> bool:
        return Heavy in self.abilities
    
    def has_pistol(self) -> bool:
        return Pistol in self.abilities
    
    def has_rapid_fire(self) -> int:
        if RapidFire1 in self.abilities:
            return 1
        elif RapidFire2 in self.abilities:
            return 2
        return 0
    
    def has_torrent(self) -> bool:
        return Torrent in self.abilities
    
    def has_sustained_hits(self) -> int:
        if SustainedHits1 in self.abilities:
            return 1
        elif SustainedHits2 in self.abilities:
            return 2
        return 0
    
    def has_lethal_hits(self) -> bool:
        return LethalHits in self.abilities
    
    def has_anti_x(self) -> tuple[Keyword, int]:
        if AntiInfantry4 in self.abilities:
            return (rules.model.Infantry, 4)
        return (None, None)
        
    def has_twin_linked(self) -> bool:
        return TwinLinked in self.abilities
        
    def has_devastating_wounds(self) -> bool:
        return DevastatingWounds in self.abilities
    
