import math
import stdio
import sys

# variables theta1, n1 and n2 are assigned value from command line argument
theta1=float(sys.argv[1])
n1=float(sys.argv[2])
n2=float(sys.argv[3])

# value is assigned to variables theta1_rad and theta2
theta1_rad=math.radians(theta1)
theta2=math.degrees(math.asin((n1*math.sin(theta1_rad))/n2))

# value of theta2 is printed as standard output
stdio.writeln(theta2)