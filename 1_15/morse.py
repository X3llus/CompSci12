#----------------------------------------------#
#               Author: Braden                 #
#              Date: 26/02/2019                #
#         Program: convert morse code          #
#----------------------------------------------#

import antigravity

def toMorse(inp): #convert to morse code
    mDict = { #morse code dictionary
        "a":".-", "b":"-...", "c":"-.-.", "d":"-..",
        "e":".", "f":"..-.", "g":"--.", "h":"....",
        "i":"..", "j":".---", "k":"-.-", "l":".-..",
        "m":"--", "n":"-.", "o":"---", "p":".--.",
        "q":"--.-", "r":".-.", "s":"...", "t":"-",
        "u":"..-", "v":"...-", "w":".--", "x":"-..-",
        "y":"-.--", "z":"--..", "1":".----", "2":"..---",
        "3":"...--", "4":"....-", "5":".....", "6":"-....",
        "7":"--...", "8":"---..", "9":"----.", "0":"-----"
    }

    morse = ""

    for i in inp: #iterate through the input and convert it
        if i == " ":
            morse += " / "
        else:
            morse += (mDict[i] + " ")
    return morse

def main(): #main function, get the input and print the morse code
    while True:
        inputVar = input("Convert to morse code:\n")
        try:
            print(toMorse(inputVar))
            break
        except KeyError:
            print("Not convertable")

main()
