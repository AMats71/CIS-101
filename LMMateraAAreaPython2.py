import random
a=1
b=20
x = random.randint(a,b)
y = random.randint(a,b)
print(x*y)
if x > 100:
    print('huge')
elif x < 100:
    print('small')
elif x == 100:
    print('just right')
