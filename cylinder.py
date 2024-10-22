import math
import stdio
import sys

r = float(sys.argv[1])
h = float(sys.argv[2])

a = 2*math.pi*r*(r+h)
v = math.pi*r*r*h

stdio.writeln("area = "+str(a))
stdio.writeln("volume = "+str(v))