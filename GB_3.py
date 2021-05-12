# Задание №1
def my_del():
    numb1 = int(input('Веедите первое число : '))
    while True:
        try:
            numb2 = int(input('Веедите второе число : '))
            result = numb1 / numb2
            return result
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

print(my_del())

# Задание №2
# Вариант 1 - данные предзаполнены
def my_card(**kwargs):
    return kwargs

print(my_card(first_name = 'Alex',
              second_name = 'Sedov',
              age = 23,
              sity = 'Moscow',
              email = 'a_sedov@gmail.com',
              num_tel = 89990000999))

# Вариант 2 - запрашиваем данные у пользователя
def my_card(**kwargs):
    return kwargs

print(my_card(name = str(input('Веедите имя : ')), surname = str(input('Введите фамилию : ')),
              age = int(input('Введите возраст : ')), sity = str(input('Введите город проживания : ')),
              email = str(input('Введите адрес электронной почты : ')), num_tel = str(input('Ведите номер телефона : '))))

# Задание №3
def my_summ(numb1, numb2, numb3):
    result = max(numb1, numb2, numb3) + max(min(numb1, numb2), min(numb1, numb3), min(numb2, numb3))
    return result

print(my_summ(34, 18, 26))

# Задание №4
# Вариант 1 — возведение в степень с помощью оператора **
def my_result(numb1, numb2):
    result = numb1 ** numb2
    return result

print (my_result(4, -6))

# Вариант 2 —  использование цикла for
def my_result(numb1, numb2):
    result = 1
    for i in range(0, numb2, -1):
        result = result * numb1
    result = 1/result
    return result

print(my_result(4, -6))

# Задание №5
def my_sum ():
    rezult = 0
    door = 'open'
    while door == 'open':
        numbers = input('Введите несколько чисел через пробел или Q для выхода: ').split()
        rez = 0
        for numb in range(len(numbers)):
            if numbers[numb].upper() == 'Q':
                door = 'close'
                break
            else:
                rez = rez + int(numbers[numb])
        rezult = rezult + rez
        print('Текущая сумма - ', rezult)
    print('Финальная сумма - ', rezult)

my_sum()

# Задание №6
def int_func():
    words = input('Input words: ')
    print(words.title())

int_func()
