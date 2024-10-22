import stdaudio
import stdio
import sys

# all the values from the file generatewaltz.py are stored here from standard input
measures=stdio.readAllInts()

# if the measures are not 32 then a message would be printed
if len(measures) !=32:
    sys.exit("A Waltz must contain 32 measures.")

# if the minuet measure is exceding 176 and lesser than 1 then a message would be printed
for i in measures[0:16]:
    if i<1 or i>176:
        sys.exit("A minuet measure must be from [1,176]")

# if the trio measure is exceding 96 and lesser than 1 then a message would be printed
for i in measures[16:32]:
    if i<1 or i>96:
        sys.exit("A trio measure must be from [1,96]")

# all the 16 minuet files associated with the numbers generated are played using data from data/M file
for v in measures[0:16]:
    filename="data/M"+str(v)
    stdaudio.playFile(filename)

# all the 16 trio files associated with the numbers generated are played using data from data/T file
for v in measures[16:32]:
    filename="data/T"+str(v)
    stdaudio.playFile(filename)