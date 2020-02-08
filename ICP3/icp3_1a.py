class Employee():

    employCount = 0
    Sum=0
    Avg =0

    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        Employee.employCount += 1
        Employee.Sum += self.salary

    def displayEmployee(self):
        print("id : ", self.id, ", Name : ", self.name, ", Salary: ", self.salary, ", department: ", self.department)


class FullTimeEmp(Employee):
    def _init_(self, id, name, salary, department):
        Employee._init_(self, id, name, salary, department)
    def displayEmployee(self):
        print("id : ", self.id, ", Name : ", self.name, ", Salary: ", self.salary, ", department: ", self.department)


employ1 = Employee(1, "bru", 100000, "eee")
employ2 = Employee(2, "sahi", 8000, "cse")
employ3=FullTimeEmp(3, "ramu", 7000,"It")


print("Total Employees %d" % Employee.employCount)
print("Average salary of the employees is", (Employee.Sum/Employee.employCount))
print(employ1.displayEmployee())
print(employ2.displayEmployee())
print(employ3.displayEmployee())