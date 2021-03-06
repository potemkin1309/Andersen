print("Задание 1")  # Составить алгоритм: если введенное число больше 7, то вывести 'Привет'

number = int(input("Введите ваше число: "))

if number > 7:
    print("Привет")

print("Задание 2")  # Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести 'Привет, Вячеслав',
# если нет, то вывести 'Нет такого имени'

name = str(input("Введите ваше имя: "))

if name == 'Вячеслав':
    print("Привет, Вячеслав")
else:
    print("Нет такого имени")

print("Задание 3")  # Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3

example_array = [9, 13, -21, 10, 4, 2, 16, 18, 8, 3, 6, 7, 8, 8, 12, 1, 7, 7, 1, 8, 4]

for i in range(len(example_array)):
    if example_array[i] % 3 == 0:
        print(example_array[i])

print("Задание 4")  # На проверку правильной скобочной последовательности.


def is_correct_brackets(text):
    while '()' in text or '[]' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')

    # Возвращаем True, если text с пустой строкой
    return not text


print(is_correct_brackets('[((())()(())]]'))
