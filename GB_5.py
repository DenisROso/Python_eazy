# Задание №1
file_name = input('Приветствую! Введите имя будущего файла: ')
file_name = file_name + '.txt'
file = open(file_name, 'w')
line = input('Излагайте свою мысль: \n')
while line:
    file.writelines(line)
    line = input('Продолжайте или нажмите "Enter" два раз для выхода: \n')
    file.write('\n')
    if not line:
        break

file.close()

# Задание №2
lines = 0
words = 0
letters = 0

for line in open('text.txt', 'r'):
    lines += 1
    letters += len(line)
    fin = 'out'
    for letter in line:
        if letter != ' ' and fin == 'out':
            words += 1
            fin = 'in'
        elif letter == ' ':
            fin = 'out'

print("Lines:", lines)
print("Words:", words)

# Задание №3
with open('mans_money.txt', 'r', encoding = 'utf-8') as f:
    mans = {}
    sum = 0
    count = 0
    rezult = 0
    for line in f:
        key, value = line.split()
        mans[key] = value
        if int(value) < 20000:
            print(f'{key} зарплата меньше 20000:', value)
        sum = sum + int(value)
        count +=1
    rezult = sum/count
    print('Средняя заработная плата составила', round(rezult, 2))

# Задание №4
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('num_word.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('num_word_2.txt', 'w') as f_2:
    f_2.writelines(new_file)

# Задание №5
while True:
    try:
        with open('file_numb.txt', 'w+') as f:
            line = input('Введите цифры через пробел: ')
            f.writelines(line)
            numb = line.split()
            print('Сумма чисел в файле =', sum(map(int, numb)))
    except ValueError:
        print('Ошибка ввовда! Введите только числа через пробел: ')
    else:
        break
    f.close()

# Задание №6
with open('words.txt', 'r', encoding='utf-8') as f:
    f_dict = {}
    for line in f:
        subject = line.split()
        numbs = []
        l = len(line)
        i = 0
        while i < l:
            s_int = ''
            a = line[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = line[i]
                else:
                    break
            i += 1
            if s_int != '':
                numbs.append(int(s_int))
        rezult = sum(numbs)
        f_dict[subject[0][:-1]] = rezult
    print(f_dict)

# Задание №7
import os, json

file = os.path.join('empresas.txt')
file_json = os.path.join('empresas.json')

result = []
profit = {}
average = []

with open(file, 'r', encoding='utf-8') as f:
    count = 1
    while True:
        line = f.readline().split()

        if not line:
            break

        profit[line[0]] = float(line[2]) - float(line[3])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        count += 1

result = [profit, {'average_profit': sum(average) / len(average)}]

with open(file_json, 'w', encoding='utf-8') as f_new:
    json.dump(result, f_new)
f_new.close()
