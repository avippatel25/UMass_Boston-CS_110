import stdio
import stdrandom

# six sided die is rolled so the outcome is assigned to variable roll
roll=stdrandom.uniformInt(1,7)

# the outcome is printed with the pattern on top side as standrad output
if roll==1:
    stdio.writeln("     ")
    stdio.writeln("  *  ")
    stdio.writeln("     ")
elif roll==2:
    stdio.writeln("*    ")
    stdio.writeln("     ")
    stdio.writeln("    *")
elif roll==3:
    stdio.writeln("*    ")
    stdio.writeln("  *  ")
    stdio.writeln("    *")
elif roll==4:
    stdio.writeln("*   *")
    stdio.writeln("     ")
    stdio.writeln("*   *")
elif roll==5:
    stdio.writeln("*   *")
    stdio.writeln("  *  ")
    stdio.writeln("*   *")
else :
    stdio.writeln("*   *")
    stdio.writeln("*   *")
    stdio.writeln("*   *")
