# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке.
# Тот, кто бьёт, здоровье не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение,
# какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

import time
import random

class Warrior:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def hit(self, enemy):
        enemy.health_down(self.damage)
        if enemy.health > 0:
            print(f'Воин {self.name} атаковал воина {enemy.name}, у воина {enemy.name} осталась {enemy.health} ед. здоровья\n'
                  f'_____________________________________________________________________')
        else:
            print(f'{self.name}:\n'
                  f"Воин {self.name} убил воина {enemy.name}\n"
                  f'_____________________________________________________________________')

    def health_down(self, damage):
        self.health -= damage

warrior_1 = Warrior("1", 100, 20)
warrior_2 = Warrior("2", 100, 20)


while warrior_1.health > 0 and warrior_2.health >0:
    choice = random.randint(1, 2)
    if choice == 1:
        warrior_1.hit(warrior_2)
    if choice == 2:
        warrior_2.hit(warrior_1)
    time.sleep(3)