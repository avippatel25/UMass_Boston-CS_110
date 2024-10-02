import math
import stdio
import sys

# variables x1, y1, x2 and y2 are assigned values from command line arguments
x1=float(sys.argv[1])
y1=float(sys.argv[2])
x2=float(sys.argv[3])
y2=float(sys.argv[4])

# value is assigned to variables x1_rad, x2_rad, y1_rad and y2_rad
x1_rad=math.radians(x1)
x2_rad=math.radians(x2)
y1_rad=math.radians(y1)
y2_rad=math.radians(y2)

# value is assigned to variable d
d = 6359.83*math.acos((math.sin(x1_rad)*math.sin(x2_rad)) + (math.cos(x1_rad)*math.cos(x2_rad)*math.cos(y1_rad - y2_rad)))

# value of d is printed as standard output
stdio.writeln(d)