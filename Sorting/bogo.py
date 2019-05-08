from random import randint, shuffle

numberList = []

#makes a list of random numbers
for n in range(6):
    numberList.append(randint(0, 100))

#function to check if the list is sorted
def isSorted(list):
    for i in range (1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True

#shuffles the list until it is sorted
def bogosort(inList):
    while not isSorted(list):
        shuffle(list)

bogosort(numberList);
