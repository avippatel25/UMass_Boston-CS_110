import math
import stdio
import sys

# variables lam and t are assigned value from command line argument
lam=float(sys.argv[1])
t=float(sys.argv[2])

# value is assigned to variable p
p=math.exp(-1*lam*t)

# p is printed as standard output
stdio.writeln(p)