import math
import stdio
import sys

# variables a, b and c are accepted as command line arguments
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

#for a quadratic equation a must not be zero
if a==0:
    stdio.writeln("Value of a must not be 0")
else:
    # also for discriminant the value should be greater than zero
    discriminant= b**2 - 4*a*c
    if discriminant<0:
        stdio.writeln("Value of discriminant must not be negative")
    else:
        # if a !=0 and discriminant is >0 than the roots are defined as
        root1= (-b+math.sqrt(discriminant))/2*a
        root2= (-b-math.sqrt(discriminant))/2*a

        # roots of quadratic equation is printed as standard output
        stdio.writeln(str(root1) +" "+ str(root2))