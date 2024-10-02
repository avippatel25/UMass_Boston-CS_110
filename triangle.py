import stdio
import sys

# variables x, y and z are assigned value from command line argument
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])

# value is assigned to variable exp
exp = x <= y + z and y <= x + z and z <= x + y

# exp is printed as standard output
stdio.writeln(exp)