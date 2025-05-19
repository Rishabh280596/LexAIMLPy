def intro(course, instructor):
    print("Welcome to", course, "course by", instructor)

intro("Python", "Rishabh Mishra")
#intro() -> # TypeError: intro() missing 2 required positional arguments: 'course' and 'instructor'
def greetings(name = "World"):
    print("Hello", name)

greetings("Rishabh")
greetings() # default value of name is used -> This would print "Hello World"

# Keyword arguments

def divide(a, b):
    return a / b

print(divide(10, 2)) # 5.0 -> Positional arguments
print(divide(b = 10, a = 5)) #-> 0.5 -> Keyword arguments

# Arbitrary arguments
# *args and **kwargs are used to pass a variable number of arguments to a function.

def add_num(*args): # Arbitrary positional arguments
    # *args is a tuple of all the positional arguments passed to the function.
    print(args) # This would print the tuple of all the positional arguments passed to the function.
    print(type(args)) # This would print the type of args which is tuple.
    print(args[1]) # This would print the second element of the tuple args.
    # print(args[5]) # This would raise an IndexError: tuple index out of range
    return sum(args)

print(add_num(1, 2, 3)) # 6 -> Positional arguments
print(add_num(1, 2, 3, 4, 5)) # 15 -> Positional arguments

def greetings2(*names):
    for name in names:
        print("Hello", name)

greetings2("Rishabh", "Mummy", "Papa", "Mona", "Kriti")

#Arbitrary keyword arguments
# **kwargs is used to pass a variable number of keyword arguments to a function.
# **kwargs is a dictionary of all the keyword arguments passed to the function.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name = "Rishabh", age = 26, company = "Qualcomm", city = "Hyderabad")
print_details(name = "Rishabh", age = 26, company = "Qualcomm", city = "Hyderabad", country = "India")