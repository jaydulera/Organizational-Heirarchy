class Employee:

    employees = []
    def __init__(self, id, name, role, reportingId, dateOfBirth, salary, allowanceClaimed, attendance):
        self.id = id
        self.name = name
        self.role = role
        self.reportingId = reportingId
        self.dateOfBirth = dateOfBirth
        self.salary = salary
        self.allowanceClaimed = allowanceClaimed
        self.attendance = attendance
        self.subordinate = []

    def addSubordinate(self, employee):
        self.subordinate.append(employee)

    @staticmethod
    def findEmployee(name):
        for employee in Employee.employees:
            if employee.name == name:
                return True
        return False

    @staticmethod
    def findManager(managerID):
        for employee in Employee.employees:
            if employee.id == managerID:
                return employee
        return None

    @staticmethod
    def indent(level):
        spaces = level
        while spaces > 0:
                print("   ", end = "")
                spaces -= 1

    @staticmethod
    def displayHeirarchy(employee, level):
        if level == 0:
            print(employee.name, " (", employee.role, ")")
        else:
            Employee.indent(level)
            print("|->", employee.name, " (", employee.role, ")")
        i = 0
        while(i < len(employee.subordinate)):
            Employee.displayHeirarchy(employee.subordinate[i], level+1)
            i += 1
