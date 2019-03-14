from database import timesheet

class Timesheet(User):

    def timesheet(self):
        # import the timesheet
        f = open(self.filename)
        # use for loop
            for hours in f:
                hours,rate = timesheet.split()
                # calculate the total
                total = hours * rate
                #return the total amount paid
                    print("Your total amount paid is", total)


