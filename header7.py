import math


# Задание 1.
# 1. Опишите класс «Тригонометрическая функция».
# Пусть функция может быть синусоидальной y=λ∙Sin(ω∙x+φ) или косинусоидальной y=λ∙Cos(ω∙x+φ).
# Данные класса: параметры λ, ω, φ, и условный тип функции: S – синус, C – косинус.
# Конструктор класса: конструктор функции с параметрами, по умолчанию: y=Sin(x), или
# y=Cos(x).
# 2. Определите методы: ввод, вычисление значения функции в указанной точке.
# 3. Перегрузите __str__ для вывода атрибутов объекта.
# 4. Напишите аксессоры и property для доступа к атрибуту «Тип функции».
# 5. Объявите два разных объекта, вычислите значения функции в произвольной точке.

class trigonometric_function:
    def __check(self):
        return self.__type_func == 0 or self.__type_func == 1

    def __init__(self, la=1, w=1, f=0, type_func=0):
        self.__l = la
        self.__w = w
        self.__f = f
        self.__type_func = type_func
        if self.__check() == 0:
            self.__type_func = 0

    def input_object(self):
        self.__l = float(input("Введите ланду: "))
        self.__w = float(input("Введите омегу: "))
        self.__f = float(input("Введите фи: "))
        self.__type_func = int(input("Введите тип функции(0-sin; 1-cos): "))
        if self.__check() == 0:
            self.__type_func = 0

    def __str__(self):
        return f'l= {self.__l}; w= {self.__w}; f= {self.__f}; type = {self.__type_func}'

    def find_func(self, x):
        if self.__type_func == 0:
            return self.__l * math.sin(self.__w * x + self.__f)
        elif self.__type_func == 1:
            return self.__l * math.cos(self.__w * x + self.__f)

    @property
    def type_func(self):
        return self.__type_func

    @type_func.setter
    def type_func(self, type_func):
        self.__type_func = type_func
        if self.__check() == 0:
            self.__type_func = 0

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, f):
        self.__f = f

    @property
    def la(self):
        return self.__l

    @la.setter
    def la(self, la):
        self.__l = la

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, w):
        self.__w = w


# Задание 2.
# 1. Опишите класс «Таблица», производный от функции. Этот класс позволит вычислять
# таблицу значений функции в указанном диапазоне x  [x0, xn], с указанным шагом изменения аргумента Δx.
# 2. Определите конструктор таблицы с параметрами, контролирующий входные данные.
# 3. Определите метод вычисления и вывода таблицы значений.
# 4. Объявите две таблицы разных функций, выведите на экран таблицы значений в одном диапазоне.
# 5. Определите две таблицы, наследующие одному базовому объекту.
class table(trigonometric_function):
    def __check(self):
        return self.__x0 < self.__xn and self.__step > 0

    def __init__(self, x0=1, xn=5, step=1, la=1.0, w=1.0, f=0.0, type_func=0):
        super().__init__(la, w, f, type_func)
        self.__x0 = x0
        self.__xn = xn
        self.__step = step
        if self.__check() == 0:
            self.__x0 = 1
            self.__xn = 5
            self.__step = 1

    def make_table(self):
        print("_________________________________")
        print(f'|\tl={self.la}; \tw= {self.w}; \tf= {self.f}\t|')
        print("|¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        for i in range(self.__x0, self.__xn, self.__step):
            print(f'|x= {i}|\ty= {super().find_func(i)}\t|')
        print("|____|__________________________|")

    def __eq__(self, other):
        return self.__x0 == other.__x0 and self.__xn == other.__xn and self.__step == other.__step and self.type_func == other.type_func

    def __str__(self):
        return f'x0 = {self.__x0}; xn = {self.__xn}; step = {self.__step}; {super().__str__()}'

    @property
    def x0(self):
        return self.__x0

    @x0.setter
    def x0(self, x0):
        self.__x0 = x0
        if self.__check() == 0:
            self.__x0 = 1
            self.__xn = 5
            self.__step = 1

    @property
    def xn(self):
        return self.__xn

    @xn.setter
    def xn(self, xn):
        self.__xn = xn
        if self.__check() == 0:
            self.__x0 = 1
            self.__xn = 5
            self.__step = 1

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step):
        self.__step = step
        if self.__check() == 0:
            self.__x0 = 1
            self.__xn = 5
            self.__step = 1
