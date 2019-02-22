#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      wolfl
#
# Created:     20-02-2019
# Copyright:   (c) wolfl 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    outf = open('DATA2.txt','w')

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    sum = 0
    su = 0
    letter = "aa"
    num = "aaaaaa"

    while len(num) == 6:
        num = raw_input('Enter a six digit number ')

    while len(letter) >= 1:
        letter = input('Enter a single letter ')

    while sum <= 10 or len(num) != 6:
        if len(num) == 6:
            for i in range(6):
                sum = sum + num(i)
                num = "0"
        else:
            switch = sum
            sum = 0
            value = switch

            for s in range(len(value):
                sum = sum + int(value(i))

    sumLetter = alphabet(sum)

    if letter == sumLetter:
        outf.write('match')
        print 'match'

    else:
        print 'error'
        outf.write('error')


main()
