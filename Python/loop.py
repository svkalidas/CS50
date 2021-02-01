
print("Python Loop")

employees = ["Kalidas", "sonia","Akash"]
employees.append("Mathews")

print(f"Employees : {employees}")

employees.sort(reverse=True)

for employee in employees:
    print(f"Employee Name : {employee}")

count = len(employees)

#While loop in python

while (count > 0):
    count = count - 1
    print(f"{count} : {employees[count]}")
