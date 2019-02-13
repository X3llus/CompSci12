#----------------------------------------------#
#               Author: Braden                 #
#              Date: 12/02/2019                #
#                Program: 1_7                  #
#----------------------------------------------#

from random import * #imports all of random

#setting up dictionary and boolean
studDict = dict()
eMarks = True

print("\nWelcome to my program")

students = int(input("\nHow many students in the class: ")) #asks for number of students

#goes through each student asking for marks
while students > 0:
    tempMark = list()
    studName = input("\nStudents name: ")

    while eMarks:
        nMark = input("\nEnter a mark or type 'next' for next student or 'random' for a random number of random marks ")

        if nMark == "next":
            break
        elif nMark.isnumeric():
            tempMark.append(int(nMark))
        elif nMark == "random":
            numOMarks = randint(1, 8)
            while numOMarks > 0:
                numOMarks -= 1
                tempMark.append(randint(0, 100))
                break
        else:
            print("\nNot a number or a valid command")

    students -= 1
    studDict.update( {(studName) : (tempMark)} )

#displays each students average than overall average
for key in studDict.keys():
    print ("\n{}'s average is {}".format(key, sum(studDict[key])/len(studDict[key]) ))
    nums = list(studDict[key])

print ("\nClass average is {}".format(sum(nums)/len(nums))) 