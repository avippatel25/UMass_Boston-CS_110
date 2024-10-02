import stdio
import sys

# variables m, d and y are assigned values from command line arguments
m=int(sys.argv[1])
d=int(sys.argv[2])
y=int(sys.argv[3])

# value is assigned to variables y0, x0, m0 and dow
y0=y-((14-m)//12)
x0=y0+(y0//4)-(y0//100)+(y0//400)
m0=m+(12*((14-m)//12))-2
dow=(d+x0+31*m0//12) % 7

# value of dow is printed as standard output
stdio.writeln(int(dow))