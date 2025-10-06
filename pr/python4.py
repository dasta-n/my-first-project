''''word = input("Введите слово: ")
result = 0
letter = " "
for n in word:
    if letter == n:
        result += 1
print(result)'''
'''word = input("ведите слово: ")
for n in range(len(word), 0, -1):
    print(word[:n])
for n in range(1, len(word)+1):
    print(word[:n])'''
'''word = input("Введите слово: ")
word = word.replace(" ", "_")
print(word)'''
numbers = []
n = int(input("Сколько чисел будет в списке: "))
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)
result = sum(numbers)
average = result / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print("Список чисел: ", numbers)
print("Сумма чисел: ", result)
print("Среднее арифметическое: ", average)
print("Максимум: ", maximum)
print("Минимум :", minimum)



