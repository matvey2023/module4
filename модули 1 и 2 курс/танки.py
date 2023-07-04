import random
import time

class Tank:
    def __init__(self, model, min_damage, max_damage, health, armor):
        self.model = model
        self.damage = random.randint (min_damage, max_damage)
        self.health = health
        self.armor = armor

    def print_info(self):
        print(f'{self.model} имеет броню {self.armor} мм'
              f' при {self.health} ед. здоровья и урон {self.damage} единиц')
    def shoot(self, enemy):
        enemy.health_down(self.damage)
        if enemy.health <= 0:
            print(f'{self.model}:'
                  f'Экипаж танка {enemy.model} уничтожен')
        else:
            print(f'{self.model}:\n'
                  f"Точно в цель, у противника {enemy.model} осталось {enemy.health} ед. здоровья\n"
                  f'_____________________________________________________________________')


    def health_down(self, damage):
        self.health -= damage//self.armor
        print(f"{self.model}:\n"
              f"Командир, по экипажу {self.model} попали, у нас осталось {self.health} ед. здоровья")

# class megaTank(Tank):
#     def __init__(self, model, min_damage, max_damage, health, armor):
#         super().__init__(model, min_damage, max_damage, health, armor)
#         self.forceArmor = True
#     def health_down(self, damage):
#         super().health_down(damage//2)

tank_1 = Tank("T-34", 500, 1500, 100, 100)
tank_1.print_info()
tank_2 = Tank("Tiger", 800, 2000, 100, 100)
tank_2.print_info()
# tank_3 = megaTank("Leopard", 1500, 2000, 100, 100)
# tank_3.print_info()

while tank_1.health > 0 and tank_2.health >0:
    choice = random.randint(1,2)
    if choice == 1:
        tank_1.shoot(tank_2)
    if choice == 2:
        tank_2.shoot(tank_1)
    time.sleep(3)

# tank_3.shoot(tank_1)
# tank_1.shoot(tank_3)