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
