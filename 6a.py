inputFile = "abc.txt"
N = int(input("Enter N value:"))

with open(inputFile, 'r') as filedata:
    linesList = [next(filedata) for _ in range(N)]

print(f"The following are the first {N} lines of the text file:")
print("".join(linesList))

word = input("Enter word to be searched: ")
k = 0

with open(inputFile, 'r') as f:
    for line in f:
        k += line.split().count(word)

print("Occurrences of the word:", k)
