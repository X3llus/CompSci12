#----------------------------------------------#
#               Author: Braden                 #
#              Date: 26/02/2019                #
#        Program: remove large blanks          #
#----------------------------------------------#

def main():
    inString = input("Give me a string with spaces:\n") #get the input
    last = ""
    newString = ""

    for i in inString: #iterate through string and remove extra spaces
        if last == " " and i == " ":
            last = i
        else:
            newString += i
            last = i

    print (newString)

main()
