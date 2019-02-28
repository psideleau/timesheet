# login class for employee
class Login:
    def __init__(self,repository):
        self.repository = repository
    def login(self,username_id,password):
        employee = self.repository.find(username_id,password)
        return employee
class Employee:    
    def __init__(self, name, employee_id):
        self.name = name
        self.id = employee_id
class Login_Repo:
    def find(self,username_id,password):
        return Employee("Alex the Employee", username_id)
login = Login(Login_Repo())
user = login.login("username", "password")
print(user.name)

#login class for supervisor
class Login:
    def __init__(self,repository):
        self.repository = repository
    def login(self,username_id, password):
        supervisor = self.repository.find(username_id,password)
        return supervisor
class Supervisor:
    def __init__(self,name,supervisor_id):
        self.name = name
        self.id = supervisor_id
class Login_Repo:
    def find(self,username_id,password):
        return Supervisor("Alex the Supervisor", username_id)
login = Login(Login_Repo())
user = login.login("username", "password")
print(user.name)

#login class for adminstrator
class Login:
    def __init__(self,repository):
        self.repository = repository
    def login(self,username_id, password):
        administrator = self.repository.find(username_id,password)
        return administrator
class Administrator:
    def __init__(self,name,administrator_id):
        self.name = name
        self.id = administrator_id
class Login_Repo:
    def find(self,username_id,password):
        return Supervisor("Alex the Administrator", username_id)
login = Login(Login_Repo())
user = login.login("username", "password")
print(user.name)





    


    
    

    
    
