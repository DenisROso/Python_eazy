# Задание №1
import time

class TrafficLight:

    def __init__(self, color_1, color_2, color_3):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3

    def running(self):
        print(f'На светофоре загорается {self.color_1} свет.')
        time.sleep(7)

        print(f'На светофоре загорается {self.color_2} свет.')
        time.sleep(2)

        print(f'На светофоре загорается {self.color_3} свет.')
        time.sleep(10)
    def unlock(self):
        print(f'На светофоре гаснут все цвета. Светофор выключен.')


svetofor = TrafficLight('красный', 'жёлтый', 'зелёный')

svetofor.running()
svetofor.unlock()

# Задание №2
# Вариант 1
class Road:

        def __init__(self, length: [int, float], width: [int, float], height: [int, float], mass):
            self._length = float(length)
            self._width = float(width)
            self._height = float(height)
            self.__mass = mass


        def asfalt_mass(self):
            self.rezult = self._length * self._width * self._height * self.__mass / 1000
            print('Для дороги длиной', self._length, 'м, шириной', self._width, 'м и толщиной дорожного покрытия',
                  self._height, 'см потребуется:', self.rezult, 'т асфальта.')

mass = 25 #кг, вес покрытия одного кв метра дороги асфальтом, толщиной в 1 см
length = input('Введите длину дорожного полотна, м: ')
width = input('Введите ширину дорожного полотна, м: ')
height = input('Введите толщину дорожного покрытия, см: ')
mass_road = Road(length, width, height, mass)
mass_road.asfalt_mass()

# Вариант 2
class Road:

    _length = 0
    _width = 0
    __mass = 25 #кг
    __height = 5 #см

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def asfalt_mass(self):
        return self._length * self._width * self.__mass * self.__height /1000


road = Road(length=4000, width=25)
print('Требуемая масса -', road.asfalt_mass(), 'т')

# Задание №3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position,  wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def full_name(self):
        return self.name + ' ' + self.surname

    def total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position('Василий', 'Рыбкин', 'Грузчик', '10000', '2000')
print(p.full_name(), p.total_income())

# Задание №4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} едет.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn_left(self):
        return f'{self.name} поворачивает влево.'

    def turn_right(self):
        return f'{self.name} поворачивает вправо.'

    def show_speed(self):
        return f'\nВы двигаетесь со скоростью {self.speed} км/ч.'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВнимание! Вы превысили рекомендемую скорость {self.speed} км/ч.'
        else:
            return f'\nВы двигаетесь с допустимой скоростью {self.speed} км/ч.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВнимание! Вы превысили рекомендемую скорость {self.speed}км/ч'
        else:
            return f'\nВы двигаетесь с допустимой скоростью {self.speed}км/ч'


class PoliceCar(Car):
    pass


town = TownCar(65, 'white', 'Lada-Kalina', 'False')
print('1:\n' + town.go(), town.show_speed(), town.turn_left(), town.turn_right(), town.stop())
sport = SportCar(200, 'Red', 'Ferrary', 'False')
print('2:\n' + sport.go(), sport.show_speed(), sport.turn_left(), sport.turn_right(), sport.stop())
work = WorkCar(35, 'gray', 'Gazelle', 'False')
print('3:\n' + work.go(), work.show_speed(), work.turn_left(), work.turn_right(), work.stop())
police = PoliceCar(90, 'green', 'UAZ-buhanka', 'True')
print('4:\n' + police.go(), police.show_speed(), police.turn_left(), police.turn_right(), police.stop())

# Задание №5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашом')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())