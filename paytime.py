from login import 
class Pay 
def __init__(self):
        self.pay = 0
        self.rate = 0
        self.hours = 0
        print("Hello, please enter your rate and hours.")
    def rate_1(self, hourly_rate):
        # hourly_rate = float(input("What is your rate: "))
        self.rate = hourly_rate
    def hours_1(self):
        timesheet_hours = float(input("What are your hours for the week: "))
        self.hours = timesheet_hours
    def show(self):
        total = self.rate * self.hours
        self.pay = total
# object class
b = Pay()
hourly_rate = float(input("What is your rate: "))

# Need to call those functions!
b.rate_1(hourly_rate)
b.hours_1()
b.show()
print("Your pay is", b.pay)
