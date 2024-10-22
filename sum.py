import stdio

a = stdio.readAllInts()

sum = 0

for i in a:
    if i%2==0:
        sum += i**2

stdio.write(sum)