import stdarray
import stdrandom
import stdio

#a 2 dimensional array is created to store the numbers in minuetMeasures of the Minuet file
minuetMeasures=stdarray.create2D(11,16)

#for loops are runed to store the values from 11x16 table given
for i in range(0,11):
    for j in range(0,16):
        minuetMeasures[i][j]=stdio.readInt()

#a 2 dimensional array is created to store the numbers in trioMeasures of the Trio file
trioMeasures=stdarray.create2D(6,16)

#for loops are runed to store the values from 6x16 table given
for i in range(0,6):
    for j in range(0,16):
        trioMeasures[i][j]=stdio.readInt()

# the 16 minuet values are printed using for loop
for j in range(0,16):
    i=stdrandom.uniformInt(1,7)+stdrandom.uniformInt(1,7)
    stdio.write(str(minuetMeasures[i-2][j])+" ")

# the 16 trio values are printed using for loop
for j in range(0,16):
    i=stdrandom.uniformInt(1,7)
    stdio.write(str(trioMeasures[i-2][j])+" ")

stdio.writeln()