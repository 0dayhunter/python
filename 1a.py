tm1 = int(input("Enter First Test Marks"))
tm2 = int(input("Enter Second Test Marks"))
tm3 = int(input("Enter Third Test Marks"))

if tm1 > tm2 and tm1 > tm3:
    if tm2 > tm3:
        avg = (tm1 + tm2) / 2
    else:
        avg = (tm1 + tm3) / 2
elif tm2 > tm1 and tm2 > tm3:
    if tm1 > tm3:
        avg = (tm1 + tm2) / 2
    else:
        avg = (tm2 + tm3) / 2
else:
    if tm1 > tm2:
        avg = (tm3 + tm1) / 2
    else:
        avg = (tm3 + tm2) / 2

print("The average of the two best test marks out of three test marks =", avg)
