class PayRoll:
    epr = 0.0
    no_of_hours = 0.0

    def __init__(self):
        self.epr = 0.0
        self.no_of_hours = 0.0

    def set_hourly_rate(self, rate):
        self.epr = rate

    def set_hours_worked(self, hours):
        while hours > 60:
            print("Error!!! Hours worked limit is 60.")
            hours = float(
                input("Enter number of hours worked less than or 60: "))

        self.no_of_hours = hours

    def calculate_pay(self):
        return self.epr * self.no_of_hours
