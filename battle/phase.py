from rules.unit import Unit
from rules.attacks import *


def shooting(attacker: Unit, rng: int, defender: Unit) -> (Unit, Unit):

    print(f'{attacker} attacks {defender} at distance {rng}')

    hits: list[tuple[Weapon, HitResult]] = [(w, hit(w, cnt, rng, defender)) for w, cnt in attacker.get_shooting(rng).items()]
    for w, h in hits:
        print(w, h)

    wounds: list[tuple[Weapon, WoundResult]] = [(w, wound(w, hit, rng, defender)) for w, hit in hits]
    for w, wnd in wounds:
        print(w, wnd)

    dmg: int = sum(damage(w, wnd, rng, defender) for w, wnd in wounds)
    print(f'{attacker} deals {dmg} damage to {defender}')

    return attacker, defender