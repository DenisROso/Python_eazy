# Задание 1
name = input('Имя: ')
surname = input('Фамилия: ')
age = int(input('Возраст: '))
print('Привет ',name, surname, age, 'лет')

# Задание 2
n = int(input('Введите время в секундах: '))
def convert(seconds):
   seconds = seconds % (24 * 3600)
   hour = seconds // 3600
   seconds %= 3600
   minutes = seconds // 60
   seconds %= 60
   return "%d:%02d:%02d" % (hour, minutes, seconds)
print(convert(n))

# Задание 3
a = int(input("Введите число a: "))
numb = str(a)
numb1 = numb + numb
numb2 = numb + numb + numb
rezult = a + int(numb1) + int(numb2)
print("Результат равен:", rezult)

# Задание 4
numb = int(input('Введите многозначное число ', ))
max = numb%10
numb = numb//10
while numb > 0:
   if numb%10 > max:
       max = numb%10
   numb = numb//10
print(max)

# Задание 5
debet = float(input("Введите сумму прибыли: "))
credit = float(input("Введите сумму расходов: "))
if debet > credit :
    rent = debet / credit
    print(f"Фирма работает успешно. Рентабельность выручки составила - {rent:.2f}")
    humans = int(input("Введите количество сотрудников фирмы "))
    bonus = rent / humans
    print(f"Прибыль в расчете на одного сотрудника составила - {bonus:.2f}")
elif debet == credit :
    print('Фирма работает без убытков и прибыли')
elif debet < credit :
    print('Фирма работает в убыток')

# Задание 6
dist = int(input("Сколько пробежал в первый в км "))
target = int(input("Сколько нужно пробежать в км "))
day = 1
while dist < target:
    dist *= 1.1
    day += 1
    print("день", day, "-", f"{dist:.2f} км")
print("Результат будет достигнут на", day, "день")