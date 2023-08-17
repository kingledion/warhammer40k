from rules.unit import Unit
from rules.attacks import *


def shooting(attacker: Unit, rng: int, defender: Unit):

    print(f'{attacker} attacks {defender} at distance {rng}')

    for w, n in attacker.get_shooting(rng).items():
        attk = Attack(w, n, rng, defender)

        test_cnt = 20000

        hits = np.zeros(test_cnt, dtype=int)
        wnds = np.zeros(test_cnt, dtype=int)
        dmg = np.zeros(test_cnt, dtype=int)
        for i in range(test_cnt):

            rslt = hit(attk)
            # print(rslt.hits)
            # print(rslt.crit_hits)
            hits[i] = np.sum(rslt.hits)

            rslt = wound(rslt, attk)
            # print(rslt.wnds)
            # print(rslt.crit_wnds)
            wnds[i] = np.sum(rslt.wnds)

            rslt = save(rslt, attk)
            # print(rslt.wnds_not_saved)
            
            d = damage(rslt, attk)
            # print(d)
            dmg[i] = d

        print(f'Deal {np.mean(hits)} hits; {np.mean(wnds)} wounds; {np.mean(dmg)} damage with {w}')



