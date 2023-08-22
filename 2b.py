def BinToDec(x):
    dec = 0
    i = 0
    while x > 0:
        r = x % 10
        if r != 0 and r != 1:
            print("Enter a valid Binary number")
            return 0
        else:
            dec += r * 2 ** i
            x = x // 10
            i += 1
    return dec

def OctaToHexa(n):
    num = n
    dec = 0
    base = 1
    temp = num
    while temp:
        r = temp % 10
        temp = temp // 10
        dec += r * base
        base = base * 8
    result = ''
    
    while dec != 0:
        temp = 0
        temp = dec % 16
        if temp < 10:
            result = str(temp) + result
        else:
            result = chr(temp + 87) + result
        dec = dec // 16
    return result

x = int(input("Enter a Binary number "))
result = BinToDec(x)
if result:
    print("The Decimal equivalent of {0} is {1}".format(x, result))

y = int(input("Enter an Octal number "))
result = OctaToHexa(y)
if result:
    print("The Hexadecimal equivalent of {0} is {1}".format(y, result))
