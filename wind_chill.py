import stdio
import sys

# variable t and v are assigned values from command line arguments
t=float(sys.argv[1])
v=float(sys.argv[2])

# variable t should have temperature less than 50 F
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")
else:
    # variable v should have speed greater than 3 mph
    if v <= 3:
        stdio.writeln("Value of v must be > 3 mph")
    else:
        #using formula of effective temperature
        w=35.74+0.6215*t+(0.4275*t - 35.75)*v**0.16

        # variable w would be printed as the standard output
        stdio.writeln(w)