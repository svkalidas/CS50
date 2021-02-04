
print("Python Loop")

employees = ["Kalidas", "sonia","Akash"]
employees.append("Mathews")

print(f"Employees : {employees}")

employees.sort(reverse=True)

print("For loop")

for employee in employees:
    print(f"Employee Name : {employee}")

count = len(employees)

#While loop in python
# in python the the nubmer 0 is interpreted as false (positive number : True and zero,negative number :False). The python 
# interpert the number as boolen only if the number is assosiated with any of the boolean operators like : not, or , and etc
print("While loop")

while (not not count):
    count = count - 1
    print(f"{count} : {employees[count]}")
