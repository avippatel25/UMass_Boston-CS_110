import stdio
import sys
import stdrandom

# variable n is assigned value from command line argument
n=int(sys.argv[1])

# value is assigned to the variable die
die_roll1=stdrandom.uniformInt(1,n+1)
die_roll2=stdrandom.uniformInt(1,n+1)

#  twice the outcome of die is printed as standard output
stdio.writeln(die_roll2+die_roll1)