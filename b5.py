num = int(input("Enter a number:"))
result_sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    result_sum += digit ** 3
    temp //= 10

if num == result_sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
