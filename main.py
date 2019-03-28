
from login import Login

def main():
    user = input("Please Enter username")
    pwd = input("Please enter password")
    user1 = Login(str(user), str(pwd))
    user1.login()
            

if __name__ == '__main__':
    main()

b = Pay()
hourly_rate = float(input("What is your rate: "))

# Need to call those functions!
b.rate_1(hourly_rate)
b.hours_1()
b.show()
print("Your pay is", b.pay)
