

import math
a = int(input ("Enter the lenght of first side: "))
b = int(input ("Enter the lenght of second side: "))
c = int(input ("Enter the lenght of third side: "))
p = ((a+b+c)/2)
Heron = (math.sqrt(p*(p-a)*(p-b)*(p-c)))
print('the area of the triangle is:', Heron)
