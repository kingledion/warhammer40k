from rules.keyword import *
from datasheets.weapon import *
from rules.model import Model

# Space Marines
Intercessor = Model(6, 4, 3, 2, 6, 2, keywords = {AdeptusAstartes, Infantry}, weapons = [BoltPistol, BoltRifle, CCW_Intercessor])

# Necrons
NecronWarrior = Model(5, 4, 4, 1, 7, 2, keywords = {Necrons, Infantry}, weapons = [GaussFlayer, CCW_NecronWarrior])