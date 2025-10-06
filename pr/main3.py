'''def say_hello():
    print("Hello")
say_hello()
say_hello()
say_hello()
def say_goodbye():
    print("Good bye")
say_goodbye()
say_goodbye()
say_goodbye()
def print_messages():
    def say_hello(): print("Hello")
    def say_goodbye(): print("Good bye")
    say_hello()
    say_goodbye()
print_messages()'''
'''def main():
    say_hello()
    say_goodbye()
def say_hello():
    print("Hello")
def say_goodbye():
    print("Good bye")
main()'''
'''def say_hello(name):
    print(f"hello, {name}")
say_hello("Tom")
say_hello("Bob")
say_hello("Alice")
def print_person(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

print_person("Tom", 37)

def say_hello(name="Tom"):
    print(f"Hello, {name}")
say_hello()
say_hello("Timur")
say_hello("Alexa")
say_hello()'''
'''def print_person(name, age):
    print(f"Name: {name}, Age: {age}")
print_person(age = 22, name = "Tom")
def print_person(name, age, *, company,):
    print(f"Name: {name} Age: {age} Company: {company}")
print_person("Bob", 41, company="Microsoft")'''
'''def print_person(name, /, age = 18, *, company="Microsoft"):
    print(f"Name: {name} Age: {age} Company: {company}")
print_person("Tom", company="JetBrains", age = 24)
print_person("Boba", 41, company = "jetget")
print_person("Bob", company ="Microsoft", age = 42)
def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")

sum(2, 4, 8, 10)
sum(1, 3, 5, 7, 9)'''
'''def sum(a, b): return a+ b
def multiply(a, b): return a * b

operation = sum
result = operation(5, 6)
print(result)
operation = multiply
print(operation(5, 6))
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
def sum(a, b): return a + b
def multiply(a, b): return a * b
do_operation(5, 4, sum)
do_operation(5, 4, multiply)
def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
operation = select_operation(1)
print(operation(10, 6))
operation = select_operation(2)
print(operation(10, 6))
operation = select_operation(3)
print(operation(10, 6))'''
