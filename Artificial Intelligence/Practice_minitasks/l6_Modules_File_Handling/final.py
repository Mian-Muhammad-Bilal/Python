import os
import re


def file_exists(f_path):
    return os.path.exists(f_path)


def count_lines(file_content):
    return len(file_content.split('\n'))


def count_words(file_content):
    words = file_content.split()
    return len(words)


def extract_emails(file_content):
    emails = re.findall(r'\S+@\S+', file_content)
    return emails


def extract_urls(file_content):
    urls = re.findall(r'http[s]?://\S+', file_content)
    return urls


def search_keywords(file_content, keyword):
    keyword_count = file_content.lower().count(keyword.lower())
    return keyword_count


while file_exists:
    f_path = input("Enter the path to the text file: ")

    if file_exists(f_path):
        print("\nFile succcessfully found...")
        print("\nReading the file...")
        with open(f_path, 'r') as file:
            f_data = file.read()
        print("\nFile reading succcessful...")
        break
    else:
        print("\nFile not found !!!\n TRY AGAIN")


while True:
    print("\n Select what do you want:")
    print("1. Count the number of lines in the file")
    print("2. Count the number of words in the file")
    print("3. Extract and display all email addresses from the file")
    print("4. Extract and display all URLs from the file")
    print("5. Search for specific keywords or phrases in the file")
    print("6. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    if choice == '1':
        print("Number of lines in the file:", count_lines(f_data))
    elif choice == '2':
        print("Number of words in the file:", count_words(f_data))
    elif choice == '3':
        emails = extract_emails(f_data)
        print("Email addresses in the file:")
        for email in emails:
            print(email)
    elif choice == '4':
        urls = extract_urls(f_data)
        print("URLs in the file:")
        for url in urls:
            print(url)
    elif choice == '5':
        keyword = input("Enter the keyword or phrase to search for: ")
        count = search_keywords(f_data, keyword)
        print(f'Occurrences of "{keyword}" in the file:', count)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")
