import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    #using prime function the prime list is created
    prime=_primes(lo,hi)
    #using sample function random number of choice is generated
    p,q=_sample(prime,2)
    n=p*q
    m=(p-1)*(q-1)
    prime2=prime[2:m]
    #while loop is used with choice function for a given length of list
    while True:
        e=_choice(prime2)
        if m%e!=0:
            break
    #while loop is used so that value of d and e for encrypt and decrypt formula is returned with value of n
    while True:
        d=stdrandom.uniformInt(1,m)
        eq=e*d%m
        if eq==1:
            break
    return n,e,d

# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return x**e%n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return y**d%n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, "0%db" % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n,2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # empty list prime is created
    prime = []
    #for loop is used to find prime numbers of the given range
    for p in range(lo, hi):
        if p < 2:
            continue
        j = 2
        #while loop is used until its divisible by 2
        while j <= (p / j):
            if p % j == 0:
                break
            j += 1
        if j > (p / j):
            prime += [p]
    return prime


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    #empty list is created of length a
    lst=a[:]
    #for loop is used until the random no of the choice is exchange of k length
    for i in range(k):
        j=stdrandom.uniformInt(i,len(a))
        temp=lst[i]
        lst[i]=lst[j]
        lst[j]=temp
    return lst[:k]


# Returns a random item from the list a.
def _choice(a):
    #l variable is given length of a
    l=len(a)
    #any random value till length of a is generated and the element of that number of a is return
    r=stdrandom.uniformInt(0,l)
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))


if __name__ == "__main__":
    _main()
