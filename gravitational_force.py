import stdio
import sys

# variables m1, m2 and r are assigned values from command line arguments
m1=float(sys.argv[1])
m2=float(sys.argv[2])
r=float(sys.argv[3])

# Value of gravitational constant G is assigned
G=6.674e-11

# value is assigned to variable f
f=G*((m1*m2)/(r*r))

# value of variable f is printed as standard output
stdio.writeln(f)