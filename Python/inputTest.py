name = input("Enter your Name :")

# here '+' is used to concat the string
print("Given name : "+name )
print(f"Entered name : {name}")

age = int(input("Enter age :"))

print(f"Age : {age}")

if age < 18 :
    print("Younger")
elif age > 18 and age <30 :
    print("Young")
else :
    print("Old")


