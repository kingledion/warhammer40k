from rules.model import *
from datasheets.weapon import *

# Space Marines
Intercessor = Model(6, 4, 3, 2, 6, 2, tags = [adeptus_astartes, infantry], weapons = [BoltPistol, BoltRifle, CCW_Intercessor])

# Necrons
NecronWarrior = Model(5, 4, 4, 1, 7, 2, tags = [necrons, infantry], weapons = [GaussFlayer, CCW_NecronWarrior])