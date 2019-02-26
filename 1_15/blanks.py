#----------------------------------------------#
#               Author: Braden                 #
#              Date: 25/02/2019                #
#               Program: 1_15                  #
#----------------------------------------------#

def main():
    inString = input("Give me a string with spaces:\n")
    last = ""
    newString = ""

    for i in inString:
        if last == " " and i == " ":
            last = i
            continue
        else:
            newString += i
            last = i
    print (newString)

main()
