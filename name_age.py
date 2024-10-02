import stdio
import sys

# variables name and age are assigned values from command line argument
name=sys.argv[1]
age=sys.argv[2]

# "name is age years old" is printed as standard output
stdio.writeln(name+" is "+str(age)+" years old.")