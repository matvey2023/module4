import random

animals=[]
for k in range(3):
    animals.append(input())

descriptions=[]
for k in range(3):
    descriptions.append(input())

for k in range(3):
    print(random.choice(descriptions) + " " + random.choice(animals))