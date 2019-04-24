import threading, sys
from random import *
from time import *

numberList = []

for n in range(10):
    numberList.append(n)

shuffle(numberList)

def isSorted(list):
    for i in range (1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True

def bozosort(list, id, threads):
    while not isSorted(List):
        shuffle(List)
        # print(numberList, id)
        # id += 1
    print(List, id, "finished")
    exit()

threads = range(1)

for t in threads:
    t = threading.Thread(target=bozosort,args=(numberList,t,threads,))
    t.start()
