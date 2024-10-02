import stdio
import sys

# variables w and h are assigned values from command line arguments
w=float(sys.argv[1])
h=float(sys.argv[2])

# value is assigned to variable bmi
bmi=w/(h*h)

# value of bmi will be printed as standard output
stdio.writeln(bmi)