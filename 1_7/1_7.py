#----------------------------------------------#
#               Author: Braden                 #
#              Date: 12/02/2019                #
#                Program: 1_7                  #
#----------------------------------------------#

import statistics as st

studDict = dict()
eMarks = True

print("\nWelcome to my program\nHelp for list of commands\n")

students = int(input("How many students in the class: "))

while students > 0:
    tempMark = list()
    studName = input("Students name: ")

    while eMarks:
        nMark = input("\ntype 'next' for next student or enter a mark ")

        if nMark == "next":
            break
        else:
            tempMark.append(nMark)

    students -= 1
    studDict.update( {(studName) : (tempMark)} )
print(studDict)

for key in studDict.keys():
    nums = list(studDict[key])
    print (st.mean(nums)) 