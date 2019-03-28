class dbFile():
    #Giving the file name where user and passwords are
    def __init__(self):
        self.filename = 'random.txt'

class User(dbFile):

    def __init__(self, username, password):
        dbFile.__init__(self)
        self.username =  username
        self.password = password
        # opens and appends in the existing file
    def addUser(self):
        with open(self.filename, 'a+') as f:
            userpass = "%s %s\n" % (self.username, self.password)
            f.write(userpass) # writes in the files
