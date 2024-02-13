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
