from rules.weapon import Weapon
from rules.keyword import Keyword

class UnitAbility:
    def __init__(self, name, val=0):
        self.name = name
        self.value = val

class Model:

    def __init__(
        self,
        m: int,
        t: int,
        sv: int,
        w: int,
        ld: int,
        oc: int,
        keywords: set[Keyword] = [],
        weapons: list[Weapon] = [],
    ):
        self.m: int = m
        self.t: int = t
        self.sv: int = sv
        self.w: int = w
        self.ld: int = ld
        self.oc: int = oc

        self.keywords: set[Keyword] = keywords
        self.weapons: list[Weapon] = weapons

    def get_toughness(self):
        return self.t
    
    def get_shooting(self, rng: int) -> list[Weapon]:

        if rng < 2:
            # also accomodate the possibility of vehicles/monsters
            return [w for w in self.weapons if w.is_pistol()]
        
        return [w for w in self.weapons if rng <= w.get_range()]
             

    def get_melee(self) -> list[Weapon]:
        
        return [w for w in self.weapons if w.get_range() == 0]
    
    def get_save(self) -> int:
        return self.sv
    
    def get_invulnerable(self) -> int:
        return 0
    
    def get_feel_no_pain(self) -> int:
        return 0
    
    def has_keyword(self, keyword) -> bool:
        return keyword in self.keywords


