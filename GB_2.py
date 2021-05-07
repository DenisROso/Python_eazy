#Задание №1
spisok = [True, 342, 56.8, 'Hello World', None, [1, 2, 3], {'first_key': 1}]
for i in spisok:
    print(type(i))

#Задание №2
spisok = input("Введите значения списка : ")
sp = spisok.split()
if len(sp) == 1:
    sp = list(spisok) #-если пользователь ввёл значения без пробелов

x = 0
for i in range(len(sp) // 2):
    sp[x], sp[x + 1] = sp[x + 1], sp[x]
    x += 2

print(sp)

# Задание №3
# Вариант с dict
while True:
    try:
        response = int(input('Введите номер месяца(число) : '))
    except ValueError:
        print('Введите номер месяца цифрой!')
    else:
        if response < 0 or response > 12:
            print('Будьте внимательнее, пожалуйста, месяцев всего 12')
        else:
            response = str(response)
            seasons = {'1': 'зима :/', '2': 'зима :/', '12': 'зима:/',
                       '3': 'весна О_о', '4': 'весна О_о', '5': 'весна О_о',
                       '6': 'лето ;)', '7': 'лето ;)', '8': 'лето ;)',
                       '9': 'осень :(', '10': 'осень :(', '11': 'осень :('}
            sr = seasons.get(response)
            print('В этом месяце на улице', sr)
            break

# Вариант с list
while True:
    try:
        response = int(input('Введите номер месяца(число) : '))
    except ValueError:
        print('Введите номер месяца цифрой!')
    else:
        if response < 0 or response > 12:
            print('Будьте внимательнее, пожалуйста, месяцев всего 12')
        else:
            seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
            print('Это время года -', seasons[response - 1])
            break

# Задание №4
text = input('Прошу Вас, излагайте свою мысль: ')
words = text.split()
x = 1
for i in words:
    letra = list(i)
    if len(letra) > 10:
        print(x, i[:11])
    else:
        print(x, i)
    x += 1

# Задание №5
# Вариант 1 - Рейтинг задан в коде. Вариант пользователя запрашивается 1 раз.
try:
    number = int(input('Введите новое число: '))
except ValueError:
    print('Введите именно целое натуральное число!')
else:
    rating = [9, 7, 5, 3, 3, 2]
    if number <= 0:
        print('Ввести можно только целые положительные числа!')
        print(rating)
    else:
        z = 0
        for i in rating:
            if rating[z] < number:
                rating.insert(z, number)
                break
            elif rating[-1] >= number:
                rating.append(number)
                break
            else:
                z += 1

            print(rating)

# Вариант 2 - Добавление элементов не ограничено. Выход из цикла предусмотрен по команде.
rating = []
while True:
    number = input('Введите новое число или наберите q для выхода: ')
    if number == 'q':
        print('Итоговый рейтинг сформирован.\n', rating)
        break
    else:
        try:
            number = int(number)
        except ValueError:
            print('Введите именно целое натуральное число!')
        else:
            if number <= 0:
                print('Ввести можно только целые положительные числа!')
            else:
                z = 0
                if len(rating) == 0:
                    rating.append(number)
                    print(rating)
                else:
                    for i in rating:
                        if rating[z] < number:
                            rating.insert(z, number)
                            break
                        elif rating[-1] >= number:
                            rating.append(number)
                            break
                        else:
                            z += 1

                    print(rating)

# Задание №6
item_list = []
item_count = 1

while True:
    print('Хотите создать новую карточку товара?')
    response = str(input('Если "да" - введите 1, если "нет" - любой другой символ: '))
    if response == '1':
        name_items = str(input('Введите наименование товара: '))
        while True:
            try:
                price_items = float(input('Введите стоимость товара, руб: '))
                break
            except ValueError:
                print('Внимание! Стоимость товара должна быть числом (возможно дробным, например 123.45).')
        while True:
            try:
                count_items = int(input('Введите количество товара: '))
                break
            except ValueError:
                print('Внимание! Введите именно целое натуральное число!')
                count_items = int(input('Введите количество товара: '))
        unit_items = str(input('Введите единицы измерения, например, шт, кг, ящ. и т.д.: '))

        item_card = (item_count, {'наименование': name_items,
                                  'стоимость': price_items,
                                  'количество': count_items,
                                  'единицы': unit_items})
        item_count += 1
        print(item_card)
        item_list.append(item_card)
    else:
        print('Карточка товара успешно сформирована.')
        break
print(*item_list, sep='\n')

analitica = dict({})
for item in item_list:
    for key, value in item[-1].items():
        if key in analitica:
            if value not in analitica.get(key):
                analitica.get(key).append(value)
        else:
            analitica.update({key: [value]})

print(f'\n Аналитика товаров: {analitica}')
reclama = analitica['наименование']
print(f'\n У нас в ассортименте: {reclama} \n Приезжайте! Покупайте!')