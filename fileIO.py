from Employee import Employee


#Creating employee object for each employee and add them to employees list
filePointer = open('emp.txt')
for line in filePointer:
    emp = line.split(",")
    if emp[3] == "NULL":
        emp[3] = -1
    if not Employee.findEmployee(emp[1]):
        employee = Employee(int(emp[0]), emp[1], emp[2], int(emp[3]), emp[4], int(emp[5]), emp[6], int(emp[7]))
        Employee.employees.append(employee)
filePointer.close()

#Assign subordinates to employees
for employee in Employee.employees:
    manager = Employee.findManager(employee.reportingId)
    if manager != None:
        manager.addSubordinate(employee)

#Display the heirarchy
Employee.displayHeirarchy(Employee.findManager(7839), 0)
