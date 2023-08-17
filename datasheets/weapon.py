from rules.weapon import *

# Space Marines
BoltPistol = Weapon("Bolt Pistol", 12, 1, 3, 4, 0, 1, {Pistol})
BoltRifle = Weapon("Bolt Rifle", 24, 2, 3, 4, -1, 1, {Assault, Heavy})
CCW_Astartes = Weapon("Close Combat Weapon", 0, 3, 3, 4, 0, 1)
AstartesGrenadeLauncher_Frag = Weapon("Astartes Grenade Launcher - frag", 24, 'd3', 3, 4, 0, 1)
AstartesGrenadeLauncher_Krak = Weapon("Astartes Grenade Launcher - krak", 24, 1, 3, 9, -2, 'd3')
Pyreblaster = Weapon("Pyreblaster", 12, 'd6', 0, 5, 0, 1)

# Necrons
GaussFlayer = Weapon("Gauss Flayer", 24, 1, 4, 4, 0, 1, {LethalHits, RapidFire1})
CCW_NecronWarrior = Weapon("Close Combat Weapon", 0, 1, 4, 4, 0, 1)