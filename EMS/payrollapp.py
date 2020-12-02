import payroll
import employees
import EmployeeManagement
import Shippments

# semp = employees.SalaryEmployee(101, "Raj", 1000)
# pemp = employees.PartTimeEmployee(102,"Ram", 50,500)
# cemp = employees.CommissionEmployee(103, "Sam", 1000,1500)

manager = employees.Manager(101, "Raj", 1000)
manager.address = Shippments.Address(101, 'DE apartments', 'bangalore', 'karnataka',560068)

developer = employees.Developer(102, "sri", 1000)
salesman = employees.SalesMan(103,"Ram", 1000,1500)
worker = employees.Worker(104, "Sam", 10 ,250)
consultant = employees.Consultant(105, "Lucky", 60, 5)

employees = [manager,developer,salesman,worker,consultant]

ems = EmployeeManagement.PerformanceManager()
ems.track(employees,40)

payroll_system = payroll.PayRoleManagementSystem()
payroll_system.calculate_payroll(employees)
