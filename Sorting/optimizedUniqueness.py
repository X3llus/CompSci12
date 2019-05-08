from random import *

#------------------------------------------------------------------------------
#Creates lists/variables
numOfNum = 10
listOrigin = []
listUnique = []
listSorted = []
listExpand = []

for i in range(numOfNum):
    listOrigin.append(randint(0, 10))

#------------------------------------------------------------------------------
#check for item in list
def checkList(x, listUnique):
    for y in listUnique:
        if x == y:
            return False
    return True

#------------------------------------------------------------------------------
#function for expanding a list
def expandList(sorted, value):
    exList = []
    for i in sorted:
        for f in range(value[i]):
            exList.append(i)
    return exList

#------------------------------------------------------------------------------
#reduces the list to unique numbers
def listOptimization(listOrigin):
    highest = max(listOrigin)
    counts = [0 for x in range(highest + 1)]

    for x in listOrigin:
        counts[x] += 1
        if checkList(x, listUnique):
            listUnique.append(x)
    return listUnique, counts

#------------------------------------------------------------------------------
listUnique, counts = listOptimization(listOrigin)

listExpand = expandList(listUnique, counts)

print(listExpand)
