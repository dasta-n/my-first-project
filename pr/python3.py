'''number = int(input("введите первое число: "))
number2 = int(input("введите второе число: "))
number3 = int(input("введите третье число: "))
if number > number2 and number > number3:
    print("Максимальное число: ", number)
elif number2 > number3:
    print("Максимальное число: ", number2)
else:
    print("Максимальное число: ", number3)'''
from operator import truediv
from timeit import repeat
from unittest import removeResult

'''word = input("Введите пароль: ")
password = "asd123"
if (word == password):
    print("Пароль верный")
else:
    print("Пароль неверный")'''

'''number = int(input("Введите число: "))
for n in range(1, 10):
    print(f"{number} * {n} = {number * n}")'''

'''minutes = int(input("Введите колличество минут: "))
hours = int(minutes / 60)
min = minutes % 60
print(f"В {minutes} минутах {hours} часов и {min}минут")'''

'''number = int(input("Введите число: "))
sum = 0
for n in range(1, number+1):
    sum += n
print(sum)'''
'''number = int(input("Угадай число: "))
num = 12
while(True):
 if number > num:
    print("число меньше")
    break
 elif number < num:
    print("число больше")
    break
 else:
    print("вы угадали число")
    break'''
word = input("Введите слово: ")
res = 0
letter = 'а'
for n in word:
    if(letter == n):
        res += 1
print(res)
