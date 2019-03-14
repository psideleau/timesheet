from login import Login

def main():
    user = input("Please Enter username")
    pwd = input("Please enter password")
    user1 = Login(str(user), str(pwd))
    user1.login()
            

if __name__ == '__main__':
    main()
