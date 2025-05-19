
a = 6
print(a)

b = 'Rishabh'
print(b)
print(b[0])

x = '10'
y = 1
print(x + str(y))  # Concatenation of string and integer after converting integer to string

p,q,r = 10,20,30
print(p,q,r)
print(p+q,q+r,r+p,p+q+r)

# Variable Naming Conventions
# 1. Variable names can only contain letters, numbers, and underscores.
# 2. Variable names cannot start with a number.
# 3. Variable names are case-sensitive.

_2 = 1
print(_2)
# 4. Variable names should not be the same as Python keywords.
# 5. Variable names should be descriptive and meaningful.
# 6. Variable names should be in lowercase, with words separated by underscores.
#$a = 1  # Invalid variable name, cannot start with a special character
# 7. Variable names should not contain spaces.
#67 = 1  # Invalid variable name, cannot start with a number
# 8. Variable names should not be the same as built-in functions or modules.

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>

B = 23.4
C = int(B)
print(C)  # 23