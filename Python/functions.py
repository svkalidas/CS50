
def square(x):
    return x*x 

class MathOperation():

    def __init__(self, a):
        self.a = a
    
    def isMultiple(self, x):
        return self.a%x == 0


a = int(input("Enter the value : "))

print(f"Square of {a} is : {square(a)}")

o = MathOperation(a)

b = int(input("Enter the factor : "))

print(f" is {a} is multiple of {b} : {o.isMultiple(b)}")