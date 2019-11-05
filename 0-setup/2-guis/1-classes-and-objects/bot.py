# Classes is Bot
class Bot:
    def __init__(self, name = "Bop", age = 40, energy = 8, shield = 4):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("*******")
        print("* {} *".format(self.name))
        print("*******")

    def display_age(self):
        print("   {}  ".format(self.age))
        print(" ******")
        print("********")
        print("********")
        print("********")

    def display_energy(self):
        total_en = int(self.energy)
        print("Energy:", total_en * "+")

    def display_shield(self):
        total_sh = int(self.shield)
        print("Shield:", total_sh * "#")

    def __str__(self):
        return ("\nName is: {} Age is: {} Energy is: {} Shield is: {}".format(self.name, self.age, self.energy, self.shield))


Bop = Bot()
Bop.display_name()
Bop.display_energy()
Bop.display_shield()
print (Bop.__str__())












