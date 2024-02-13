import PRclass


def main():
    n = int(input("Enter the number of employees: "))
    PR_list = [PRclass.PayRoll() for j in range(n)]

    for i in range(n):
        print(f"\nEnter details for Employee no.{i + 1}:")
        epr = float(input("Enter hourly pay rate: "))
        no_of_hours = float(input("Enter number of hours worked: "))
        PR_list[i].set_hourly_rate(epr)
        PR_list[i].set_hours_worked(no_of_hours)

    print("\nPayroll Results:")
    for i in range(n):
        total_pay = PR_list[i].calculate_pay()
        print(f"Total Pay of Employee no.{i + 1} is \"{total_pay}\"")


main()
