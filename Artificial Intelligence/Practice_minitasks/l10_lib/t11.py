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
get_day_of_week('2023-12-05')
