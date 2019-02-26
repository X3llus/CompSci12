#----------------------------------------------#
#               Author: Braden                 #
#              Date: 26/02/2019                #
#               Program: 1_15                  #
#----------------------------------------------#

def rot13Conv(inp):
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghidklm")
    return str.translate(inp, table)

def main():
    inpStr = input("What to encrypt (ROT13):\n")
    print (rot13Conv(inpStr))

main()
