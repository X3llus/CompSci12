def conversion():
    print("nothing yet")

def check(inp):
    if len(inp) == 8:
        if int(inp[0]+inp[1]) <= 12:


def main():

    date = list()
    tempDate = list()
    tempInt = 0
    tempStr = ""
    month = {
    "01":"January", "02":"February",
    "03":"March", "04":"April",
    "05":"May", "06":"June",
    "07":"July", "08":"August",
    "09":"September", "10":"October",
    "11":"November", "12":"December"
    }

    while True:
        tempStr = str(input("Give me a date (MMDDYYYY):\n"))




    date.append(tempStr[2]+tempStr[3]) #day
    date.append(tempStr[0]+tempStr[1]) #month
    date.append(tempStr[4]+tempStr[5]+tempStr[6]+tempStr[7]) #year

    print ("{}".format(month[date[0]]))

    return 0

main()
