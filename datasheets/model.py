from rules.keyword import *
from datasheets.weapon import *
from rules.model import Model

# Space Marines
Intercessor = Model(6, 4, 3, 2, 6, 2, keywords = {AdeptusAstartes, Infantry}, weapons = [BoltPistol, BoltRifle, CCW_Astartes])
Intercessor_GrenadeFrag = Model(6, 4, 3, 2, 6, 2, keywords = {AdeptusAstartes, Infantry}, weapons = [BoltPistol, AstartesGrenadeLauncher_Frag, CCW_Astartes])
Intercessor_GrenadeKrak = Model(6, 4, 3, 2, 6, 2, keywords = {AdeptusAstartes, Infantry}, weapons = [BoltPistol, AstartesGrenadeLauncher_Krak, CCW_Astartes])
Infernus = Model(6, 4, 3, 2, 6, 1, keywords = {AdeptusAstartes, Infantry}, weapons = [BoltPistol, Pyreblaster, CCW_Astartes])

# Necrons
NecronWarrior = Model(5, 4, 4, 1, 7, 2, keywords = {Necrons, Infantry}, weapons = [GaussFlayer, CCW_NecronWarrior])