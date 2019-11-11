# Code to demonstrate inheritance
#from SuperBot import *
from bot import Bot
from SuperBot import Superbot
from FlyingBot import Flyingbot
#display_name, display_age, display_energy
bop = Bot("Bop", 1, 2, 3)
bop.display_name()
bop.display_age()
bop.display_energy()
bop.display_shield()

superbop = Superbot("SuperBop", 11, 12, 13, 14)
superbop.display_name()
superbop.display_age()
superbop.display_energy()
superbop.display_shield()
superbop.display_super_power_level()

flyingbop = Flyingbot("FlyingBop", 22,23, 24, 25, 26)
flyingbop.display_name()
flyingbop.display_age()
flyingbop.display_energy()
flyingbop.display_shield()
flyingbop.display_super_power_level()
flyingbop.display_hover_distance()




