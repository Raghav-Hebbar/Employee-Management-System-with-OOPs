import payroll
import employees
import EmployeeManagement

# semp = employees.SalaryEmployee(101, "Raj", 1000)
# pemp = employees.PartTimeEmployee(102,"Ram", 50,500)
# cemp = employees.CommissionEmployee(103, "Sam", 1000,1500)

manager = employees.Manager(101, "Raj", 1000)
developer = employees.developer(102, "sri", 1000)
salesman = employees.salesman(103,"Ram", 1000,1500)
worker = employees.Worker(104, "Sam", 10,2500)

employees = [manager,developer,salesman,worker]

ems = EmployeeManagement.PerformanceManager()
ems.track(employees,40)

payroll_system = payroll.PayRoleManagementSystem()
payroll_system.calculate_payroll(employees)
