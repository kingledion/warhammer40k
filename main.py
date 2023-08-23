from datasheets.model import *
from rules.unit import Unit
from battle.phase import *
import battle.benchmark_phase as bmp

def main():

    intercessor_squad = Unit("Intercessor Squad", (Intercessor, 10))
    infernus_squad = Unit("Pyreblaster Squad", (Infernus, 10))
    inceptor_squad_bolter = Unit("Inceptor Squad (Assault Bolters)", (Inceptor_Bolter, 3))


    necron_warriors = Unit("Necron Warriors", (NecronWarrior, 20))

    bmp.shooting(inceptor_squad_bolter, 12, necron_warriors)

    

if __name__ == "__main__":
    main()





