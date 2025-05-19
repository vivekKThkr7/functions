
x = lambda a: a + 10
print(x(5))


multiply = lambda a, b: a * b
print(multiply(5, 6)) 

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  

def myfunc(n):
    return lambda a: a * n

doubler = myfunc(2)
print(doubler(11))  # Output: 22

tripler = myfunc(3)
print(tripler(11))  # Output: 33


def fibonacci_recursive(x):
    # Base cases
    if x == 0:
        return 0
    if x == 1:
        return 1
    # Recursive case
    return fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2)

fib_numbers = [fibonacci_recursive(i) for i in range(10)]
print(fib_numbers)

def create_multiplier(factor):
    # This inner function is a closure that "remembers" the factor
    def multiply(number):
        return number * factor
    return multiply

# Create specialized functions
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15


def calculate_area(radius):
    import math
    return math.pi * radius ** 2



def greeting():
    return "Hello, world!"
say_hello = greeting
print(say_hello())  

operations = [lambda x, y: x + y, lambda x, y: x - y]
print(operations[0](5, 3))  # Output: 8
print(operations[1](5, 3))  # Output: 2

