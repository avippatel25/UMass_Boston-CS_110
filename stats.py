import stdio
import sys
import stdrandom

# variables a and b are assigned value from command line argument
a=int(sys.argv[1])
b=int(sys.argv[2])

# random value is assigned to variables x1, x2 and x3
x1=stdrandom.uniformFloat(a,b)
x2=stdrandom.uniformFloat(a,b)
x3=stdrandom.uniformFloat(a,b)

# value is assigned to variables mean, var and str_var
mean=(x1+x2+x3)/3
var=((x1-mean)**2+(x2-mean)**2+(x3-mean)**2)/3
std_dev=var**0.5

# 'mean var std_var' is printed as standard output
stdio.writeln(str(mean)+" "+str(var)+" "+str(std_dev))