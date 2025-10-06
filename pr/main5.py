'''def outer():
    n = 5
    def inner():
        nonlocal n
        n += 1
        print(n)

    return inner
fn = outer()
fn()
fn()
fn()
def multiply(n): return lambda m: n * m

fn = multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))'''
'''def select(input_func):
    def output_func():
        print("****************")
        input_func()
        print("****************")
    return output_func()
@select
def hello():
    print("Hello Metanit.com")


def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]
        if age < 0: age = 1
        input_func(name, age)

    return output_func


@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 38)
print_person("Bob", -5)'''