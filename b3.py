def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
