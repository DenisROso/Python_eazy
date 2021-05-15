# Задание №1
print('Добро пожаловать в скрипт рассчёта заработной платы!')
job_hour = float(input('Введите время работы ,ч: '))
money_hour = float(input('Введите ставку, р/ч: '))
percent = float(input('Введите процент премии: '))

def my_money():
    money = job_hour * money_hour
    percentes = (percent * money) / 100.0
    rezult = money + percentes
    return rezult

print('Ваша заработная плата составила', round(my_money(), 2), 'рублей.')

# Задание №2
from random import randint

list = [randint(1, 100) for i in range(15)]
print(list)

new_list = []
for i in range(len(list) - 1):
    n = list[i]
    i += 1
    m = list[i]
    if m > n:
        new_list.append(m)

print(new_list)

# Задание №3
print(f'{[el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]}')

# Задание №4
from random import randint

list = [randint(1, 10) for i in range(20)]
new_list = [el for el in list if list.count(el) < 2]

print(list, new_list, sep='\n')

# Задание №5
import operator
import functools

list = [el for el in range(100, 1001) if el % 2 == 0]
rezult = functools.reduce(operator.mul, list)

print(list)
print(rezult)

# Задание №6
# Первая часть задания c "count"
# Вариант 1
from itertools import count

for i in count(1):
    if i > 5:
        break
    else:
        print(i)

# Вариант 2
from itertools import islice, count

for i in islice(count(1), 7):
    print(i)

# Вторая часть задания c "cycle"
# Вариант 1
from itertools import cycle

count = 0
for item in cycle('Hello!'):
    if count > 11:
        break
    print(item)
    count += 1

# Вариант 2
from itertools import islice, cycle

for i in islice(cycle("Hello!"), 6):
    print(i)

# Задание №7
def fact(n):
    numbs = 1
    for i in range(1, n + 1):
        numbs *= i
        yield numbs

n = int(input('Введите число: '))
for _ in fact(n):
    print(_)
