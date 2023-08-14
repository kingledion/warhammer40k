from itertools import chain
from collections import Counter

from rules.model import Model
from rules.weapon import Weapon

class Unit:
    def __init__(self, name: str, *members: tuple[Model, int]):
        self.name: str = name
        self.members: list[Model] = []
        for m, cnt in members:
            self.members.extend([m] * cnt)
        if len(self.members) < 1:
            raise Exception("Unable to instatiate a unit without any member Models")

    def __str__(self) -> str:
        return self.name
    
    def get_shooting(self, rng: int) -> Counter[Weapon, int]:
        weapons: list[Weapon] = list(chain(*[model.get_shooting(rng) for model in self.members]))
        return Counter(weapons)

    def get_melee(self) -> Counter[Weapon, int]:
        weapons: list[Weapon] = list(chain(*[model.get_melee() for model in self.members]))
        return Counter(weapons) 
    
    def get_members(self) -> list[Model]:
        return self.members
    
    def get_target(self) -> Model:
        return self.members[0]