    
import datetime
import calendar

class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self,id,name,rate_per_day):
        super().__init__(id,name)
        self.rate_per_day = rate_per_day

    def calculate_payroll(self):
        today = datetime.datetime.now()
        totalDays = calendar.monthrange(today.year,today.month)[1]
        return self.rate_per_day * totalDays

class PartTimeEmployee(Employee):
    def __init__(self,id, name, total_hours,rate_per_hour):
        super().__init__(id,name)
        self.total_hours = total_hours
        self.rate_per_hour = rate_per_hour

    def calculate_payroll(self):
        return self.total_hours * self.rate_per_hour


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, rate_per_day,commission):
        super().__init__(id, name, rate_per_day)
        self.commission = commission

    def calculate_payroll(self):
        salary = super().calculate_payroll()
        return salary + self.commission

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} Manager is handling team for {hours} hours")

class developer(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} developer is handling team for {hours} hours")

class salesman(CommissionEmployee):
    def work(self,hours):
        print(f"{self.name} as salesman is handling the client calls for {hours} hours")

class Worker(PartTimeEmployee):
    def work(self, hours):
        print(f"{self.name} as worker has completed his task in {hours} hours")


class consultant(developer, PartTimeEmployee):
    def __init__(self,id,name,total_hours,rate_per_hour):
        PartTimeEmployee.__init__(self,id,name,total_hours,rate_per_hour)

    def calculate_payroll(self):
        return PartTimeEmployee.calculate_payroll(self)