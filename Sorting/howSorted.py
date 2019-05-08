from random import *
import math

#------------------------------------------------------------------------------
#Finds percentage of how sorted a list is based on how far each character is
#from it's sorted position
def howSorted(unsorted):

    max = findMaxScore(sorted)
    current = 0

    for i in range(len(unsorted)):
        for x in range(len(unsorted)):
            if sorted[i] == unsorted[x]:
                current += abs(x - i)

    percentSorted = math.ceil(((max - current) / max) * 100)

    print("The list is {}% sorted".format(percentSorted))

#------------------------------------------------------------------------------
#Finds the max score of the list
def findMaxScore(list):

    bestScore = 0

    for i in range(len(list)):
        #First half of the list
        if len(list) - i - 1 > len(list) - (len(list) - i):
            bestScore += len(list) - i - 1

        #Second half of the list
        elif len(list) - i - 1 <= len(list) - (len(list) - i):
            bestScore += len(list) - (len(list) - i)

    return bestScore

#------------------------------------------------------------------------------
#main stuff
def main():

    sortedList = []
    unsortedList = []

    for n in range(6):
        sortedList.append(n)
        unsortedList.append(n)

    shuffle(unsortedList)

    print("sorted list: {}\nunsorted list: {}".format(sortedList, unsortedList))


    howSorted(sortedList, unsortedList)

#------------------------------------------------------------------------------

main()
