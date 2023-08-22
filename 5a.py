def isphonenumber(x):
    if len(x) != 12:
        return 0
    else:
        for i in range(0, 12):
            if i == 0 or i == 1 or i == 2:
                if not x[i].isdigit():
                    return 0
            if i == 4 or i == 5 or i == 6:
                if not x[i].isdigit():
                    return 0
            if i == 8 or i == 9 or i == 10:
                if not x[i].isdigit():
                    return 0
            if i == 3 or i == 7:
                if x[i] != "-":
                    return 0
        return 1

def REisphonenumber(x):
    import re
    pno = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = pno.search(x)
    if mo is None:
        return 0
    else:
        return mo.group()

if __name__ == '__main__':
    phoneNo = input("Enter a phone number of ddd-ddd-dddd format to validate: ")
    ch = int(input("Enter 1 to validate without RE, 2 to validate using RE: "))

    if ch == 1:
        if isphonenumber(phoneNo) == 1:
            print("You have entered a valid phone number")
        else:
            print("You have entered an invalid phone number")
    elif ch == 2:
        if REisphonenumber(phoneNo) == 1:
            print("You have entered a valid phone number")
        else:
            print("You have entered an invalid phone number")
