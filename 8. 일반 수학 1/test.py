import math

x = int(input())

a = 1
b = 1
c = -x * 2

r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)



print(math.ceil(r1))