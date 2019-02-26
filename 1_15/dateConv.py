#----------------------------------------------#
#               Author: Braden                 #
#              Date: 25/02/2019                #
#               Program: 1_15                  #
#----------------------------------------------#

def check(inp): #check inputs to make sure the date is correct
    if len(inp) == 8:
        m = int(inp[0]+inp[1])               #month
        d = int(inp[2]+inp[3])               #day
        y = int(inp[4]+inp[5]+inp[6]+inp[7]) #year
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12: #checks for months with 31 days
            if d <= 31:
                return True
        elif m == 4 or m == 6 or m == 9 or m == 11: #checks for months with 30 days
            if d <= 30:
                return True
        elif m == 2:
            if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0): #checks if it is a leap year
                if d <= 29:
                    return True
            else:
                if d <= 28:
                    return True
        else:
            return False

def main(): #main function

    date = list() #the date
    tempStr = ""  #just a temporary string
    month = {     #dictionary for converting numbers to months
    "01":"January", "02":"February",
    "03":"March", "04":"April",
    "05":"May", "06":"June",
    "07":"July", "08":"August",
    "09":"September", "10":"October",
    "11":"November", "12":"December"
    }

    while True: #input loop
        tempStr = str(input("Give me a date (MMDDYYYY):\n"))

        if check(tempStr): #calls check function to check input
            break
        else:
            print("\nIncorrect Date.\n")

    date.append(tempStr[2]+tempStr[3])                       #day
    date.append(tempStr[0]+tempStr[1])                       #month
    date.append(tempStr[4]+tempStr[5]+tempStr[6]+tempStr[7]) #year

    print ("{} {} {}".format(int(date[0]), month[date[1]], date[2]))

main()
