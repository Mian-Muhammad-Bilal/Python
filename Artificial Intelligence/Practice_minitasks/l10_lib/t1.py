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
