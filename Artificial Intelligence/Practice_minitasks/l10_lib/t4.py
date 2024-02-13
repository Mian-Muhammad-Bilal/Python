import sys


def print_command_line_arguments():

    if len(sys.argv) > 1:
        print("Command-line arguments:")
        for x in sys.argv[1:]:
            print(x)
    else:
        print("No command-line arguments provided.")


print_command_line_arguments()
