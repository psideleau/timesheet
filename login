from database import User

class Login(User):

    def login(self):
        # opening the user password file
        with open(self.filename) as f:
            # spilting the text in lines
            data = f.readlines()
            # Going through file line by line
            for usepass in data:
                user, pwd = usepass.split()
                # matching the credentials
                if (self.username == user and self.password == pwd):
                    print("Login Successfully")
                    return True
        # If login failed then call adduser function
        print("Login Failed")
        #print("Adding user")
        self.addUser()
        
