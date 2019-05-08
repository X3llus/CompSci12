from random import shuffle, randint
from sys import argv

#------------------------------------------------------------------------------
# Checks if a list is sorted
def isSorted(list):
    for i in range(1, len(list)):
        if(list[i - 1] > list[i]):
            return False
    return True

#------------------------------------------------------------------------------
# Breaks a list into blocks, bogosorts them, then merges them back together
def bogoBlock(array):
    blockSize = 5;  # Magic konstant
    blocks = list()
    outArray = list()
    scratchArray = list()
    blockIndex = 0;

    # Slice the list into blocks
    while blockIndex < len(array):
        blocks.append(list(array[blockIndex:blockIndex + blockSize]))
        blockIndex += blockSize

    # Bogosort each block
    for block in blocks:
        while not isSorted(block):
            shuffle(block)

    # Stack-merge the blocks into one big list again
    for block in blocks:
        if len(outArray) == 0:
            outArray = list(block)
            continue
        else:
            scratchArray = list(outArray)
            outArray = list()
        while len(scratchArray) > 0 or len(block) > 0:
            if len(scratchArray) == 0:
                outArray.extend(block)
                break
            elif len(block) == 0:
                outArray.extend(scratchArray)
                break
            elif scratchArray[0] <= block[0]:
                outArray.append(scratchArray.pop(0))
            elif block[0] < scratchArray[0]:
                outArray.append(block.pop(0))

    return outArray

#------------------------------------------------------------------------------
# Main function
def main():
    length = 10  # Default list length
    if (len(argv) >= 2):
        length = int(argv[1])
        print("Building a {}-element list.".format(length))
    else:
        print("No length specified. Building a 10-element list.")

    # Create random array using list comprehension
    array = [randint(0, 100) for i in range(length)]

    print(array)
    print(bogoBlock(array))

main()
