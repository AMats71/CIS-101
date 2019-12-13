#take an input
#2 random, 1,6
#matches user input
import random

answer = int(input("what value do you want to roll to?"))
total = 0
times = 0

while answer != total:
    x = random.randint(1,6)
    y = random.randint(1,6)
    total = x + y
    #times = times + 1
    times += 1

print("you rolled the dice " + str(times) + " times")
