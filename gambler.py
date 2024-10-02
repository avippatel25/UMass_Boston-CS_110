import stdio
import sys

# variables n1, n2 and p are assigned values from command line arguments
n1=int(sys.argv[1])
n2=int(sys.argv[2])
p=float(sys.argv[3])

# value is assigned to variables q, p1 and p2
q=1-p
p1=(1-((p/q)**n2))/(1-((p/q)**(n1+n2)))
p2=(1-((q/p)**n1))/(1-((q/p)**(n1+n2)))

# 'p1 p2' is printed as standard output
stdio.writeln(str(p1)+" "+str(p2))