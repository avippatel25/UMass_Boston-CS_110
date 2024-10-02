import math
import stdio
import sys

# variables r and theta are assigned values from command line arguments
r=float(sys.argv[1])
theta=float(sys.argv[2])

# value is assigned to variables v, x and y
v=theta*(math.pi/180)
x=r * math.cos(v)
y=r * math.sin(v)

#  'x y' is printed as standard output
stdio.writeln(str(x)+" "+str(y))