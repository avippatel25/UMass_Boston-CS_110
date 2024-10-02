import stdio
import sys

# variables t and v are assigned value from command line argument
t=float(sys.argv[1])
v=float(sys.argv[2])

# value is assigned to variable w
w=35.74+0.6215*t+(0.4275*t-35.75)*(v**0.16)

# w is printed as the standard output
stdio.writeln(w)