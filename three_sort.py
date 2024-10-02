import stdio
import sys

# variables x, y and z are assigned value from comment line argument
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])

# value is assigned to variables mn, mx and a
mn=min(x,y,z)
mx=max(x,y,z)
a=(x+y+z)-(mn+mx)

# 'mn a mx' is printed as standard output
stdio.writeln(str(mn)+" "+str(a)+" "+str(mx))