# 1) Number addition
def add_numbers(a, b):
    return a + b 
    
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")

# 2) Full name 
def full_name(fname, lname):
    return fname + " " + lname

firstName = input("Enter First name: ")
lastName = input("Enter Last name: ")
name = full_name(firstName, lastName)
print(f"The name is {name}")
