numbers = []
reverse = []
n = int(input("Сколько чисел будет в списке: "))
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)
print("Исходный список: ", numbers)
result = sum(numbers)
average = result / len(numbers)
maximum = max(numbers)
minimum = min(numbers)
negative = sum(1 for num in numbers if num < 0)
print("Сумма чисел: ", result)
print("Среднее арифметическое:", average)
print("Максимальное число: ", maximum)
print("Минимальное число: ", minimum)
print("Колл-во отрицательных чисел: ", negative)
for l in range(len(numbers)):
    reverse.append(numbers [-l -1])
print(reverse)
numbers = [num for num in numbers if num % 2 != 0]
print("Список без четных чисел: ", numbers)