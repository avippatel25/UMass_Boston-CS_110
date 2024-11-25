import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture

# Entry point
def main():
    # values are accepted as command line arguments
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    pics = sys.argv[4:]

    # using for loops and beadfinder file of python the bead is tracked and the distance is calculated to see where the blob is traveled in the given picture
    blob_f = BlobFinder(Picture(pics[0]), tau)
    lastBeads = blob_f.getBeads(pixels)
    # for loop is used until the length of the picture
    for i in range(1,len(pics)):
        blob_f = BlobFinder(Picture(pics[i]),tau)
        curBeads = blob_f.getBeads(pixels)

        #for loop is used for each elements in current bead
        for cur_bead in curBeads:
            closest_distance = math.inf
            closest_bead = None

            #for loop is used for each elements in last bead
            for last_bead in lastBeads:
                distance = cur_bead.distanceTo(last_bead)
                if distance <= delta and distance < closest_distance:
                    closest_distance = distance
                    closest_bead = last_bead

            # the value of the nearest bead is then returned as standard output
            if closest_distance != math.inf:
                stdio.write(f"{closest_distance:.4f}\n")

        stdio.writeln()
        lastBeads = curBeads

if __name__ == "__main__":
    main()
