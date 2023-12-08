import math
x=math.sqrt(54)
print(x)


y=math.ceil(1.4)
z=math.floor(2.4)

print(y)
print(z)


#para brindar un numero random
import random

print(random.randrange(2,100))

print(random.randrange(2,100,step=2))

lista=[1,2,"coder",13,56]
string="esta cadena de caracteres"

print(random.choice(lista))
print(random.choice(string.split()))