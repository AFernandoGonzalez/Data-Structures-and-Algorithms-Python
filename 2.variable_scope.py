
# https://www.w3schools.com/python/python_scope.asp

a = 15
b = 25

def my_function():
    global a
    a = 11
    b = 21

my_function()
print(a)
print(b)