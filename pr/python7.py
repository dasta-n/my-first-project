'''class Person:
    def say(self, message):
        print("message")
tom = Person()
tom.say("Hello METANIT.COM")'''
from anyio import sleep_forever

from python4 import result

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")
tom = Person("Tom", 22)
tom.display_info()
bob = Person("Bob", 43)
bob.display_info()'''
'''class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")
tom = Person("Tom", 39)
tom.__name = "Spider Man"
tom.__age = 18
tom.print_person()'''
'''class Phone:
    def __init__(self, model, number):
        self.model = model
        self.number = number
    def display_info(self):
        print(f"Модель: {self.model}\t Номер: {self.number}")
    def call(self):
        print(f"Звонок на номер {self.number}")
cell = Phone ("Iphone", 8800)
cell.display_info()
cell.call()'''
'''class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def model_info(self):
        print(f"Марка: {self.brand} Год: {self.year}")

car1 = Car("Audi", 2001)
car1.model_info()
car2 = Car("Tesla", 2023)
car2.model_info()'''
'''class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self, a, b):
        result = a + b
    def multiply(self, a, b):
        result =  a * b
    def minus(self, a, b):
        result = a - b
    def divide(self, a, b):
        result = a / b
num = Calculate(6, 7)
num.plus()'''
