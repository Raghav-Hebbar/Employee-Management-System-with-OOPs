class PerformanceManager():
    def track(self, employees, hours):
        print("Tracking Employee Performance")
        print("=============================")

        for employee in employees:
            #employee.work(hours)
            status = employee.work(hours)
            print(f"{employee.name} : {status}")
            print("-----------------------------")
            
class ManagerRole:
    def work(self,hours):
        return f" Manager is handling the project team for {hours} hours"

class DeveloperRole:
    def work(self,hours):
        return f"developer is handling team for {hours} hours"

class SalesRole:
    def work(self,hours):
        return f"as salesman is handling the client calls for {hours} hours"

class WorkerRole:
    def work(self,hours):
        return f"worker has completed his task in {hours} hours"