# Напишите программу, которая эмулирует знаменитую игру “Орёл или решка”.
# Программа должна запросить у пользователя что он выбирает и далее сказать, победил ли он или проиграл.
import random

v=["орел", "решка"]
user_variant=input("Орел или решка? ")
user_variant=user_variant.lower()
comp_variant=random.choice(v)
if user_variant==comp_variant:
    print("Ты выиграл!")
else:
    print("Не получилось угадать :(")
