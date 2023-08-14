from datasheets.model import *
from rules.unit import Unit
from battle.phase import *

def main():

    attacker = Unit("Intercessor Squad", (Intercessor, 10))
    defender = Unit("Necron Warriors", (NecronWarrior, 20))

    shooting(defender, 12, attacker)

    

if __name__ == "__main__":
    main()





