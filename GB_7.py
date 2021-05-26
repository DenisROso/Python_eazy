# Задание №1
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list


    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f'{i:4}', end='')
            print()
        return ''

    def __str__(self):
        return '\n'.join(map(str, self.my_list))


    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

m = Matrix([[-3, 2, 1], [-1, 0, 1], [0, -1, -1], [1, 1, 5]])
new_m = Matrix([[4, 0, -2], [-2, 3, 0], [0, 3, 2], [-2, 2, -5]])
print(m.__add__(new_m))

# Задание №2
print('Добро пожаловать в ателье "Funny buttons"!\n '
      'Мы можем изготовить для Вас пальто и костюм.')
import math
from abc import ABC, abstractmethod

class AbsractOdezda(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def material(self):
        pass

class Odezda(AbsractOdezda):

    def __init__(self):
        pass

    @property
    def tkan_vsego(self):
        tkan = math.fsum([raschet_palto.material(), raschet_costum.material()])
        return str(f'Всего потребуется {tkan :.2f} метра ткани')

    def material(self):
        pass


class Palto(Odezda):
    def __init__(self, razmer):
        self.razmer = razmer
        super().__init__()

    def material(self):
        return self.razmer / 6.5 + 0.5


class Costum(Odezda):
    def __init__(self, rost):
        self.rost = rost
        super().__init__()

    def material(self):
        return self.rost / 100 * 2 + 0.3

while True:
    try:
        get_razmer = float(input('Введите размер (США - от 0 до 30): '))
        break
    except ValueError:
        print('Введите размер числом!')
while True:
    try:
        get_rost = float(input('Введите рост в сантиметрах: '))
        break
    except ValueError:
        print('Введите размер числом!')

raschet_palto = Palto(get_razmer)
raschet_costum = Costum(get_rost)
cosa = Odezda()
print(f'На пальто требуется {raschet_palto.material():.2f} метра ткани')
print(f'На костюм требуется {raschet_costum.material():.2f} метра ткани')
print(cosa.tkan_vsego)
print('Благодарим за выбор нашего ателье!')

# Задание №3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Клетки объединились. Теперь размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка уменьшилась. Теперь размер клетки равен: {sub}' if sub > 0 else 'Клетка уничтожена.'

    def __truediv__(self, other):
        return f'Клетка разделилась. Теперь размер клетки равен: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Клетки умножились. Теперь размер клетки равен: {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += f'{"*" * row} \n'
        result += f'{"*" * (self.quantity % row)}'
        return result


cell = Cell(15)
cell_2 = Cell(3)

print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(4))
