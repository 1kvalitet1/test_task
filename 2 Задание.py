"""
Задача 2. Написать функцию/метод, которая на вход получает массив положительных
целых чисел произвольной длины. Например [42, 12, 18].
На выходе возвращает массив чисел, которые являются
общими делителями для всех указанных числе. В примере это будет [2, 3, 6].
"""


def common_divisor(massive=None):
    if massive is None:
        massive = [42, 12, 18]

    raw_massive = []
    massive_divisor = []
    try:
        if isinstance(massive, list):
            for element in massive:
                if isinstance(element, int):
                    i = 1
                    while i <= element:
                        i += 1
                        if element % i == 0:
                            massive_divisor.append(i)
                    raw_massive.append(massive_divisor)
                    massive_divisor = []

                else:
                    return 'Не все элементы массива integer'

            for raw_element in range(len(raw_massive)):
                raw_massive[raw_element] = set(raw_massive[raw_element])

            intersection_set = raw_massive[0]
            for row in raw_massive[1:]:
                intersection_set &= row
            if not intersection_set:
                return f'Нет общих делителей: {intersection_set}'
            return intersection_set
        else:
            return 'Тип переменной не list'
    except Exception as e:
        return 'Произошла не предвиденная ошибка:', e


print(common_divisor())
print(common_divisor([400, 100, 200, 300, 10000]))
print(common_divisor([800, 4, 200, 894, 315]))
print(common_divisor([800, '4', 200, 894, 315]))
