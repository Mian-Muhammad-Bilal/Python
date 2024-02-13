import re


def extract_emails(txt):
    formate = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(formate, txt)
    return emails


text = input("Enter the text containing the email address: ")
mail = extract_emails(text)

if mail:
    print("Extracted Email Addresses:")
    for x in mail:
        print(x)
else:
    print("The text not contains any Email Addresses")
