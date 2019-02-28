#----------------------------------------------#
#               Author: Braden                 #
#              Date: 26/02/2019                #
#               Program: ROT13                 #
#----------------------------------------------#

def rot13Conv(inp): #converts the string to ROT13 (rotates characters by 13)
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz"
    , "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghidklm")
    return str.translate(inp, table)

def main(): #gets input and prints the encrypted string
    inpStr = input("What to encrypt (ROT13):\n")
    print (rot13Conv(inpStr))

main()
