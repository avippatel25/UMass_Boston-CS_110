import stdio

# a is assigned value from standard input
a=stdio.readAllStrings()

# n is given the length of a
n=len(a)

#for loop is runed till n/2 to exchange the first and last elements
for i in range(0,n//2):
    a[i],a[n-i-1] = a[n-i-1],a[i]

# for loop is runed till n and then the value is printed in correct format
for i in range(0,n):
    if i < n-1:
        stdio.write(a[i]+" ")
    else:
        stdio.writeln(a[i])