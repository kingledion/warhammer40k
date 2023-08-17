from rules.unit import Unit
from rules.attacks import *


def shooting(attacker: Unit, rng: int, defender: Unit) -> (Unit, Unit):

    print(f'{attacker} attacks {defender} at distance {rng}')

    for w, n in attacker.get_shooting(rng).items():
        attk = Attack(w, n, rng, defender)

        rslt = hit(attk)
        #print(rslt.hits)
        #print(rslt.crit_hits)

        rslt = wound(rslt, attk)
        #print(rslt.wnds)
        #print(rslt.crit_wnds)

        rslt = save(rslt, attk)
        #print(rslt.wnds_not_saved)

        dmg = damage(rslt, attk)

        print(f'Deal {np.sum(dmg)} damage with {w}')



