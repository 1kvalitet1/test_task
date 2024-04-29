"""
Задача 3. Написать функцию/метод, которая возвращает массив простых чисел
в диапазоне (2 числа - минимальное и максимальное) заданных чисел.
Например, на вход переданы 2 числа: от 11 до 20
(диапазон считается включая граничные значения).
"""


def range_numbers_simple(number_1=11, number_2=20):
    raw_massive = []

    try:
        if isinstance(number_1, int) and isinstance(number_2, int):
            for value in range(number_1, number_2+1):

                boolean = True
                i = 1
                while i < value:
                    i += 1
                    if value % i == 0 and value != i:
                        boolean = False
                        break
                if boolean and value not in raw_massive:
                    raw_massive.append(value)

            if raw_massive[0] == 0:
                return raw_massive[2:]
            if raw_massive[0] == 1:
                return raw_massive[1:]

            return raw_massive
        else:
            return 'У одной или более  переменной тип не integer'

    except Exception as e:
        return 'Произошла не предвиденная ошибка:', e


print(range_numbers_simple())
print(range_numbers_simple(0, 200))
print(range_numbers_simple(1, 400))
print(range_numbers_simple(900, 1000))
print(range_numbers_simple(1000, 900))
