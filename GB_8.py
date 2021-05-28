# Задание №1
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        list = []

        if 1 > day or day > 31:
            list.append(f'Ошибка! значение "день" введено неверно.')
        if 1 > month or month > 12:
            list.append(f'Ошибка! значение "месяц" введено неверно.')
        if 0 >= year:
            list.append(f'Ошибка! значение "год" введено неверно.')
        if len(list) > 0:
            return " ".join(list)
        else:
            return f'Введены верные значения даты.'

    def __str__(self):
        return f'Текущая дата - {Data.extract(self.day_month_year)}'


today = Data('11 - 1 - 2001')
print(today)

print(Data.valid(11, 11, 2022))
print(today.valid(45, 13, -11))

print(Data.extract('8 - 2 - 1996'))
print(today.extract('27 - 5 - 2021'))


# Задание №2
class New_Exc(Exception):

    def del_func(self, x, y):
        while True:
            try:
                rezult = x / y
            except ZeroDivisionError:
                print(f'Внимание, ошибка! На ноль делить нельзя!')
                y = float(input('Ведите делитель: '))
            else:
                print(f'{x} / {y} = {rezult:.2f}')
                break


x = float(input('Введите делимое: '))
y = float(input('Ведите делитель: '))

a = New_Exc()
a.del_func(x, y)


# Задание №3
class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        val = int(input('Введите число, затем нажмите Enter: '))
        self.my_list.append(val)
        print(f'Текущий список - {self.my_list} \n ')
        while True:
            val = input('Введите следующее число, затем нажмите Enter или нажмите Q для выхода : ')

            if val == 'Q' or val == 'q':
                print(f'Текущий список - {self.my_list} \n ')
                return f'Создание списка завершено. Выход.'
            else:
                try:
                    val = int(val)
                    self.my_list.append(val)
                    print(f'Текущий список - {self.my_list} \n ')
                except:
                    print(f"Внимание! Недопустимое значение - строка и(или) булево.")


try_except = Error()
print(try_except.my_input())


# Задание №4(5,6)
class Warehouse:

    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            x = self._dict.setdefault(name).pop(0)
            print('{} отправляется заказчику'.format(x))


class Equipment:

    def __init__(self, name, serial_num, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.serial_num = serial_num
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.serial_num} {self.make} {self.year}'


class Printer(Equipment):

    def __init__(self, name, serial_num, make, year):
        super().__init__(name, serial_num, make, year)
        self.name = name
        self.serial_num = serial_num
        self.make = make
        self.year = year

    def __repr__(self):
        return f'{self.name} {self.serial_num} {self.make} {self.year}'

    def action(self):
        return 'Принтер печатает.'


class Scanner(Equipment):

    def __init__(self, name, serial_num, make, year):
        super().__init__(name, serial_num, make, year)
        self.name = name
        self.serial_num = serial_num
        self.make = make
        self.year = year

    def action(self):
        return 'Сканер сканирует.'


class Xerox(Equipment):

    def __init__(self, name, serial_num, make, year):
        super().__init__(name, serial_num, make, year)
        self.name = name
        self.serial_num = serial_num
        self.make = make
        self.year = year

    def action(self):
        return 'Ксерокс Копирует.'


sklad = Warehouse()

scanner = Scanner('HP', 99811347, '321', 2016)
sklad.add_to(scanner)
scanner = Scanner('Canon', 10714135, '311', 2013)
sklad.add_to(scanner)
scanner = Scanner('Sony', 11909090, '330', 2015)
sklad.add_to(scanner)
printer = Printer('Epson', 16161617, '112', 2017)
sklad.add_to(printer)
xerox = Xerox('LG', 13232324, '400', 2017)
sklad.add_to(xerox)

print(sklad._dict)

sklad.extract('Scanner')
print()
print(sklad._dict)