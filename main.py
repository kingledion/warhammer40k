from datasheets.model import *
from rules.unit import Unit
from battle.phase import *
import battle.benchmark_phase as bmp

def main():

    attacker = Unit("Intercessor Squad", (Intercessor, 10))
    defender = Unit("Necron Warriors", (NecronWarrior, 20))

    bmp.shooting(attacker, 12, defender)

    

if __name__ == "__main__":
    main()





