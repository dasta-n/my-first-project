'''message = lambda: print("hello")
message()
sum = lambda n, m: n + m
print(sum(4, 5))
print(sum(5, 6))

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
do_operation(5,4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)

def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b
operation = select_operation(1)
print(operation(10, 6))
operation = select_operation(2)
print(operation(10, 6))
operation = select_operation(3)
print(operation(10, 6))'''
'''def say_hi():
    global name
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)
def say_bye():
    print("Good bye", name)

say_hi()
say_bye()'''

'''def outer():
    n = 5
    def inner():
        print(n)
    inner()
    print(n)
outer()

def outer():
    n = 5
    def inner():
        n = 25
        print(n)
    inner()
    print(n)
outer()
def outer():
    n = 5
    def inner():
        nonlocal n
        n = 25
        print(n)
    inner()
    print(n)
outer()'''
