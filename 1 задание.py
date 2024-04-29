"""
Задача 1. Разработайте функцию, которая принимает целое число в качестве
аргумента и возвращает строку,содержащую это число и слово "компьютер"
в нужном склонении по падежам в зависимости от числа.
Например, при вводе числа 25 функция должна возвращать "25 компьютеров",
для числа 41 — "41 компьютер", а для числа 1048 — "1048 компьютеров".
"""


def numbers_computer(number=1):
    end_symbol = ''
    try:
        if isinstance(number, int):
            str_number = str(number)
            if len(str_number) >= 2:

                if str(str_number[0]) != '1' and len(str_number) == 2:
                    str_number = str_number[-1]
                elif str(str_number[-2]) != '1' and len(str_number) > 2:
                    str_number = str_number[-1]
                else:
                    end_symbol = 'ов'

            if len(str_number) == 1:
                if str_number in ('2', '3', '4'):
                    end_symbol = 'а'
                if str_number in ('0', '5', '6', '7', '8', '9'):
                    end_symbol = 'ов'

            return f'{number} компьютер{end_symbol}'
        else:
            return 'Тип переменной не integer'

    except Exception as e:
        return 'Произошла не предвиденная ошибка:', e


for x in range(0, 10001):
    print(numbers_computer(x))
