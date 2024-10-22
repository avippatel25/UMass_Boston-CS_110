import stdarray
import stdio
import stdrandom
import sys

# set value of 365 to variable days_per_year
days_per_year = 365

# new variavle trials has assigned value as command line argument
trials = int(sys.argv[1])

# 0 is assigned to variable count
count = 0

# for loop is used till the range of trials
for t in range(trials):
    birthdays = stdarray.create1D(days_per_year, False)
    # while loop is runed infinitely
    while True:
        # value of count is increased evry time the loop is runed
        count += 1
        # random int value is given
        birthday = stdrandom.uniformInt(0, days_per_year)
        # if the birthday value is found in birthdays than the loop is broken or else it is assigned value true
        if birthdays[birthday]:
            break
        else:
            birthdays[birthday] = True

# value of count/trial is printed as standard output
stdio.writeln(count // trials)