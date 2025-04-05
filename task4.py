class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours == None:
            return cls(name, (7 - rest_days)*8, rest_days, email)
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email == None:
            return cls(name, hours, rest_days, f"{name}@email.com")
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        if self.hours != None: 
            return self.hours * self.hourly_payment
        
get_hours = EmployeeSalary.get_hours("test", 31, 5, "test")
print(get_hours.name, get_hours.hours, get_hours.rest_days, get_hours.email, get_hours.hourly_payment, get_hours.salary())

EmployeeSalary.set_hourly_payment(300)
print(EmployeeSalary.hourly_payment)

get_email = EmployeeSalary.get_email("test", 31, 5, None)
print(get_email.name, get_email.hours, get_email.rest_days, get_email.email, get_email.hourly_payment, get_email.salary())