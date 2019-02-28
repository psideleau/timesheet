class Payroll

def __init__(self, standard_hours,overtime_hours):
    self.standard_hours = int (standard_hours)
    self.overtime_hours = int (overtime_hours)
    

def calculator (hours,rate):

    if hours < 40:
        standard_hours = hours
        overtime_hours = 0
    else:
        standard_hours = 40
        overtime_hours = hours - 40

    if hours > 40:
        overtimerate = 2.0 * rate
        overtime = (hours-40) * overtimerate
    else:
        overtime = 0

    return standard_hours, overtime_hours

