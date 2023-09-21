class Palindrome:
    def check(self, s):
        s = str(s)
        if s == s[::-1]:
            print("\nIt is Palindrome")
        else:
            print("\nIt is Not Palindrome")

if __name__ == '__main__':
    while True:
        print("Enter 1. For String palindrome")
        print("Enter 2. For Integer Palindrome")
        print("Enter 3. To Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            text = input("Enter a string to check: ")
            p = Palindrome()
            p.check(text)
        elif ch == 2:
            text = input("Enter a number to check: ")
            p = Palindrome()
            p.check(text)
        elif ch == 3:
            break
        else:
            print("Invacarlid choice")
