x = int(input("Enter a number: "))
c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
num = x
rev = 0

while x > 0:
    r = x % 10
    rev = rev * 10 + r
    x = x // 10

    if r == 0:
        c0 += 1
    elif r == 1:
        c1 += 1
    elif r == 2:
        c2 += 1
    elif r == 3:
        c3 += 1
    elif r == 4:
        c4 += 1
    elif r == 5:
        c5 += 1
    elif r == 6:
        c6 += 1
    elif r == 7:
        c7 += 1
    elif r == 8:
        c8 += 1
    elif r == 9:
        c9 += 1

if rev == num:
    print("The Number {0} is palindrome ".format(num))
else:
    print("The Number {0} is not palindrome ".format(num))

print("The occurrence of 0 is {0}, 1 is {1}, 2 is {2}, 3 is {3}, 4 is {4}, 5 is {5}, 6 is {6}, 7 is {7}, 8 is {8}, 9 is {9}".format(c0, c1, c2, c3, c4, c5, c6, c7, c8, c9))
