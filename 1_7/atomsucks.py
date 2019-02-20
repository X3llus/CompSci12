#-------------------------------------------------------------------------------
# Name:        Python Knowledge
# Purpose:
#
# Author:      Timmy Thorpe
#
# Created:     15/02/2019
#-------------------------------------------------------------------------------

import math

num = 3
testFactors = [2]
prime = False

number = 1000000

for x in range(3, number):
    x = 0
    composite = False

    while testFactors[x] <= math.sqrt(num) and not composite:
        if num % testFactors[x] == 0:
            composite = True
        x += 1

    if not composite:
        testFactors.append(num)

    num += 1

print (testFactors)