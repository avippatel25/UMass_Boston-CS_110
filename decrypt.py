import rsa
import stdio
import sys


# Entry point.
def main():
    # n and e variable are assigned value as command line argument
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # width is given number of bits per character for encryption
    width = rsa.bitLength(n)

    # message is given value as standard input
    message = stdio.readAll()

    #the length of the message variable is giveen to i
    i=len(message)

    # for loop is used for encryption of every character in message given
    for i in range(0,i-1,width):
        s = message[i:i + width]
        y = rsa.bin2dec(s)
        x = rsa.decrypt(y, n, d)
        stdio.write(chr(x))


if __name__ == "__main__":
    main()
