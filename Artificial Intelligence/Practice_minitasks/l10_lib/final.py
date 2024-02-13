##############TASK NO.1
import os
def file_exists(f_path):
    return os.path.exists(f_path)

f_path = input("Enter the path to the text file: ")
if file_exists(f_path):
    print("\nFile succcessfully found...")
    size = os.path.getsize(f_path)
    print(f"The file exists. Size: {size} bytes.")
else:
    print("\nFile does not exist on this sepecific path !!!\n")

# input file path: /home/bilal/Documents/UMT/semmester5/code/AI/AI/l10/t1.py
#OUTPUT: File succcessfully found...
#        The file exists. Size: 426 bytes.

#================================================================================================
##############TASK NO.2
import shutil
import sys

def copy_file(source_path, destination_path):
    shutil.copy(source_path, destination_path)
    print(f"File copied from {source_path} to {destination_path}.")
copy_file(sys.argv[1], sys.argv[2])

# SHOULD BE RUN LIKE THIS: python -u "/home/bilal/Documents/UMT/semmester5/code/AI/AI/l10/t2.py" /home/bilal/Documents/UMT/semmester5/code/AI/AI/l10/t1.py /home/bilal/Documents/UMT/semmester5/code/AI/AI/
#OUTPUT: File copied from /home/bilal/Documents/UMT/semmester5/code/AI/AI/l10/t1.py to /home/bilal/Documents/UMT/semmester5/code/AI/AI/.

#================================================================================================
##############TASK NO.3
import glob

def list_of_txt_files():
    txt_files = glob.glob('*.txt')
    if txt_files:
        print("List of .txt files in the current directory:")
        for i in txt_files:
            print(i)
    else:
        print("No .txt files found in the current directory.")

list_of_txt_files()

#================================================================================================
##############TASK NO.4
import sys
def print_command_line_arguments():

    if len(sys.argv) > 1:
        print("Command-line arguments:")
        for x in sys.argv[1:]:
            print(x)
    else:
        print("No command-line arguments provided.")
print_command_line_arguments()

#================================================================================================
##############TASK NO.5
import argparse

def add_integers(num1, num2):
    return num1 + num2

def main():
    parser = argparse.ArgumentParser()  # Creating ArgumentParser object
    parser.add_argument('num1', type=int)
    parser.add_argument('num2', type=int)
    args = parser.parse_args()  # Parsing arguments

    sum = add_integers(args.num1, args.num2)
    print(f"The sum of {args.num1} and {args.num2} is: {sum}")

main()

#================================================================================================
##############TASK NO.6
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
#================================================================================================
##############TASK NO.7
import math

def calculate_circle_area(radius):
    area = (math.pi * (radius**2))
    return area

Radius = int(input('Enter the radius to calculate the circle area: '))
area = calculate_circle_area(Radius)
print(f"The area of a circle with radius {Radius} is: {area}")
#================================================================================================
##############TASK NO.8
import random
import string

def generate_random_password():
    # Combine letters and digits
    characters = string.ascii_letters + string.digits
    # Generate a random password of length 8 from characters
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

print(f"Generated random password: {generate_random_password()}")
#================================================================================================
##############TASK NO.9
import statistics

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 1111]

print(f"Mean: {statistics.mean(numbers)}")
print(f"Median: {statistics.median(numbers)}")
#================================================================================================
##############TASK NO.10
import urllib.request

def download_image(url, filename):
    try:
        print(f"\nDownloading image...")
        with urllib.request.urlopen(url) as img:
            image = img.read()
            with open(filename, 'wb') as file:
                file.write(image)

        print(f"Image downloaded successfully and saved as {filename}")
    except Exception as e:
        print(f"Error downloading image: {e}")

image_url = input("Enter/Paste image url: ")
# EXAMPLE: 'https://online.umt.edu.pk/img/UMT_Logo.png'
local_filename = 'image.jpg'
download_image(image_url, local_filename)
#================================================================================================
##############TASK NO.11
from datetime import datetime

def get_day_of_week(date_str):
    try:
        date_object = datetime.strptime(date_str, "%Y-%m-%d")

        day_of_week = date_object.weekday()

        days_of_week = ["Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday", "Saturday", "Sunday"]
        print(
            f"The day of the week for {date_str} is {days_of_week[day_of_week]}")
    except ValueError:
        print(f"Invalid date format. Please use 'YYYY-MM-DD'.")

# date = input("Enter a date i.e(2023-12-06): ")
get_day_of_week('2023-12-09')
#================================================================================================
##############TASK NO.13
import timeit


def sum_numbers():
    return sum(range(1, 1001))


execution_time = timeit.timeit(sum_numbers, number=100000)

print(f"Execution time for sum_numbers function: {execution_time:.5f} seconds")
