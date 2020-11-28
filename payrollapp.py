import payroll

semp = payroll.SalaryEmployee(101, "Raj", 1000)
pemp = payroll.PartTimeEmployee(102,"Ram", 50,500)
cemp = payroll.CommissionEmployee(103, "Sam", 1000,1500)

payroll_system = payroll.PayRoleManagementSystem()
payroll_system.calculate_payroll([semp, pemp, cemp])
