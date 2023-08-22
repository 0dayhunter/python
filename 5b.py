import re

try:
    file = open("data.txt")
    for line in file:
        line = line.strip()
        
        # Extract and print phone numbers
        phone_numbers = re.findall(r"\d{10}", line)
        if len(phone_numbers) > 0:
            print("Phone numbers:", phone_numbers)
        
        # Extract and print email addresses
        emails = re.findall(r"[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+", line)
        if len(emails) > 0:
            print("Emails:", emails)
            
except FileNotFoundError as e:
    print(e)
