import time
import check_file
import count_lines
import count_words
import emails
import urls
import search
import parser_menu
import save_file

while check_file.file_exists:
    f_path = input("Enter the path to the text file: ")

    if check_file.file_exists(f_path):
        print("\nFile succcessfully found...")
        time.sleep(1)
        print("\nReading the file...")
        with open(f_path, 'r') as file:
            f_data = file.read()
        time.sleep(1)
        print("\nFile reading succcessful...")
        break
    else:
        print("\nFile not found !!!\n TRY AGAIN")

while True:
    parser_menu.menu()
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    if choice == '1':
        print("\n==========================\nNumber of lines in the file:",
              count_lines.count_lines(f_data), "\n==========================")
    elif choice == '2':
        print("\n==========================\nNumber of words in the file:",
              count_words.count_words(f_data), "\n==========================")
    elif choice == '3':
        emails = emails.extract_emails(f_data)
        print("Email addresses in the file:\n")
        print("==========================")
        for email in emails:
            print(email)
        print("==========================")
    elif choice == '4':
        urls = urls.extract_urls(f_data)
        print("URLs in the file:")
        print("==========================")
        for url in urls:
            print(url)
        print("==========================")
    elif choice == '5':
        keyword = input(
            "\n==========================\nEnter the keyword or phrase to search for: ")
        count = search.search_keywords(f_data, keyword)
        print(
            f'\n==========================\nOccurrences of "{keyword}" in the file:', count, "times \n==========================\n")
    elif choice == '6':
        output_file = input("Enter the name of the output file: ")
        tosave = email, urls, keyword
        save_file.save_results_to_file(tosave, output_file)
        print(f"Results saved to {output_file}")
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please select a valid option.")
