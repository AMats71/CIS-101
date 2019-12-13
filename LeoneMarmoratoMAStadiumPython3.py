'''
Antonino L-M Matera
'''
import random

secA = int(input('how many for section A?'))

def secAprice(a):
    priceA = 150*a
    print('with ' + str(a) + " people it will cost " + str(priceA))
    return priceA

valueA = secAprice(secA)

secB = 3

def secBprice(b):
    priceB = 100*b
    print('with ' + str(b) + " people it will cost " + str(priceB))
    return priceB

valueB = secBprice(secB)

secC = random.randint(0,10)

def secCprice(c):
    priceC = 50*c
    print('with ' + str(c) + " people it will cost " + str(priceC))
    return priceC

valueC = secCprice(secC)

total = valueA+valueB+valueC
print('Grand total is ' + str(total))

if total > 1000:
    print('You will receive a 10% discount!')

discounttotal = total*.1
print('your discounted amount is ' + str(discounttotal))
