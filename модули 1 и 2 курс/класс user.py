import random

class User:
    def __init__(self, health):
        self.health = health
        self.damage = random.randint(50, 100)

    def attack(self, enemy):
        enemy.health -= self.damage

class Magician (User):
    def __init__(self, health):
        super().__init__(self, health)
    def attack(self, enemy):
        super().attack(self.damage * 4)

class Warrior (User):
    def __init__(self, health,):
        super().__init__(self, health)
    def attack(self, enemy):
         super().attack(self.damage * 3)


class Archer (User):
    def __init__(self, health):
        super().__init__(self, health)
    def attack(self, enemy):
         super().attack(self.damage * 2)

archer1 = Archer(100)
warrior1 = Warrior(150)

archer1.attack(warrior1)