import math
import stdio

#global variables with the values are assigned
ETA = 9.135e-4
RHO = 0.5e-6
T = 297
R = 8.31457

# Entry point.
def main():
    #two variables are assigned 0 as value
    var = 0
    n = 0
    #while loop is used until its empty and the displacement is given the vaue
    while not stdio.isEmpty():
        displacements = stdio.readFloat()
        displacement_mtr = displacements * 0.175e-6
        var += displacement_mtr ** 2
        n += 1

    #using the given formulas the value of var and k are assigned and then avogadros constant value is formed
    var = var / (2 * n)
    k = 6 * math.pi * var * ETA * RHO / T

    avogadro_constant = R / k

    # avogadros constant value is returned
    stdio.writef("%e\n", avogadro_constant)


if __name__ == "__main__":
    main()
