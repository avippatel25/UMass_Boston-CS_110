import math

import stdarray
import stdio
import sys

# variable n is assigned int value as command line argument
n=int(sys.argv[1])
# new list x is created
x=[]

# for loop is runed till the range of n and value is added to list
for i in range(0,n):
    x += [stdio.readFloat()]

# new list y is created
y=[]

# for loop is runed till the range of n and value is added to list
for i in range(0, n):
    y += [stdio.readFloat()]
# value is assigned t0 distance
distance = 0.0

# for loop is runed till range of n and the value of (x-y)^2 is added to distance
for i in range(0,n):
    distance += (x[i] - y[i])**2

# value of sqrt of distance is printed
stdio.writeln(math.sqrt(distance))