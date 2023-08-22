x = input("Enter a sentence: ")
y = x
print("There are", len(x.split()), "words in the sentence")

digits = 0
upper = 0
lower = 0

for i in x:
    if i.isdigit():
        digits += 1
    elif i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("There are {0} digits, {1} uppercase characters, and {2} lowercase characters in the sentence".format(digits, upper, lower))
