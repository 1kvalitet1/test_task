"""
Задача 4. Написать метод, который в консоль выводит таблицу умножения.
На вход метод получает число, до которого выводит таблицу умножения.
В консоли должна появиться таблица. Например, если на вход пришло число 5,
то получим(таблицу 5*5):
"""


def numbers_multiplication(number=5):
    try:
        multiplication_massive = []
        raw_massive = []
        if isinstance(number, int):
            for x in range(1, number + 1):
                raw_massive.append(x)
                if x == 1:
                    raw_massive.insert(0, " ")

            multiplication_massive.append(raw_massive)
            raw_massive = []
            print()

            for value in range(1, number + 1):
                raw_massive.insert(0, value)

                for val in range(1, number + 1):
                    raw_massive.append(value * val)
                multiplication_massive.append(raw_massive)
                raw_massive = []

            for row in multiplication_massive:
                for element in row:
                    print("{:2}".format(element), end=" ")
                print()
            print()
            return multiplication_massive
        else:
            return 'Тип переменной не соответсвует integer'

    except Exception as e:
        return 'Произошла не предвиденная ошибка:', e


print(numbers_multiplication())
print()
print(numbers_multiplication(10))
print()
