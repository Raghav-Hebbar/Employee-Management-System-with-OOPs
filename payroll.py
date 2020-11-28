
class PayRoleManagementSystem:

    def calculate_payroll(self,employees):
        print("Payroll Management Syaytem")
        print("===============================")

        for employee in employees:
            print(f"Employee #: {employee.id}\nEmployee Name :{employee.name}")
            print(f"Amount : {employee.calculate_payroll()}")
            print("----------------------------------------")


