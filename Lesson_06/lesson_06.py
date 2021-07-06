
"""Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

 Общая информация:
 версия Python 3.8
 разрядность ОС 64
 """


from collections import Mapping, Container
from sys import getsizeof

# функция взята в попытке разобраться в выделением памяти для списков и т.п.
# использование будет описано позже
def deep_getsizeof(o, ids):
    """Find the memory footprint of a Python object

    This is a recursive function that drills down a Python object graph
    like a dictionary holding nested dictionaries with lists of lists
    and tuples and sets.

    The sys.getsizeof function does a shallow size of only. It counts each
    object inside a container as pointer only regardless of how big it
    really is.

    :param o: the object
    :param ids:
    :return:
    """
    d = deep_getsizeof
    if id(o) in ids:
        return 0

    r = getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str):  # or isinstance(o, unicode):
        return r

    if isinstance(o, Mapping):
        return r + sum(d(k, ids) + d(v, ids) for k, v in o.iteritems())

    if isinstance(o, Container):
        return r + sum(d(x, ids) for x in o)

    return r

def equation_of_a_straight_line(x1, y1, x2, y2):
    """По введенным пользователем координатам двух точек вывести уравнение прямой вида
        y = kx + b, проходящей через эти точки."""

    coefficient_a = y1 - y2
    coefficient_b = x1 - x2
    coefficient_c = x1 * y2 - x2 * y1
    print(f' Уравнение прямой для точек {x1, y1} и {x2, y2} выглядит \n следующим образом'
          f'  {coefficient_a}x + {coefficient_b}y + {coefficient_c} = 0')

    """
    Переменные:
    x1, y1, x2, y2, coefficient_a, coefficient_b, coefficient_c

    Теоретически семь переменных int должны занимать 4 * 7 + 24 * 7 = 196 bit
    """

    # Считаем память
    sum_mem = 0
    mem = 0
    for i in (x1, y1, x2, y2, coefficient_a, coefficient_b, coefficient_c):
        mem = getsizeof(i)  # размер конкретной переменной
        sum_mem += mem
        print(f'{mem} + ', end='')
    print(f' = {sum_mem}')
# Так и выходит 28 + 28 + 28 + 28 + 28 + 28 + 28 +  = 196


def ascii_table(start=32, stop=127, column_n=10):
    """5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
    заканчивая 127-м включительно. Вывод выполнить в табличной форме:
    по десять пар "код-символ" в каждой строке."""

    for i in range(column_n):  # Печатаем заголовок таблицы
        print('   code  -  simbol  ', end='')
    print()
    column_n_count = 0  # Счётчик колонок
    corrector_space = '    '  # Количество пробелов для 2-х значных кодов
    for i in range(start, stop):  # Перебираем символы
        if len(str(i)) >= 3:
            corrector_space = '   '  # Количество пробелов для 3-х значных кодов
        print(f'{corrector_space}{i}   -    {chr(i)}     ', end='')  # Выводим значения
        column_n_count += 1  # Считаем колонки
        if not column_n_count % column_n:  # переводим стоку по количеству колонок
            print()

    """
    Переменные:
    start, stop, column_n, i, column_n_count, corrector_space = '    '
    
    Теоретически 5 переменных int + 1 str длинною 4 символа
    5 * 4 + 5 * 24 + 37 + 1 * (4 + 1) = 183
        
    """
    print()
    # Считаем память
    sum_mem = 0
    mem = 0
    for i in (start, stop, column_n, i, column_n_count, corrector_space):
        mem = getsizeof(i)  # размер конкретной переменной
        sum_mem += mem
        print(f'{mem} + ', end='')
    print(f' = {sum_mem}')

    # реально получается 28 + 28 + 28 + 28 + 28 + 52 +  = 192
    # где-то промахнулись со строкой, она должна быть 42
    # >>> sys.getsizeof('    ')
    # 53
    # >>> sys.getsizeof('')
    # 51
    # sys.getsizeof(' ')
    # 50                   - странные какие-то цифры
    # задание выполнялось в PyCharm в чистой консоли Python 3.8.2 Shell цифры те же.
    # Не могу объяснить, если честно. Прочитал нескольно статей, например:
    # https://code.tutsplus.com/ru/tutorials/understand-how-much-memory-your-python-objects-use--cms-25609
    # https://habr.com/ru/post/193890/ - это та, с которой, видимо была сделана методичка
    # но, если принять что в этой версии питона накладные расходы формируются по другом, то остальное правильно


def multiplicity(start=2, finish=99, start_d=2, finish_d=9):  # Сделал входные параметры для универсальности
    """1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
    каждому из чисел в диапазоне от 2 до 9."""

    res = [0 for _ in range(finish_d)]
    index = [i + start_d for i in range(finish_d)]  # Делители будут использоваться в выводе результата
    for i in range(start_d, finish_d):
        for k in range(start, finish):
            if k % i:
                pass  # решил, что использование NOT в условии это лишняя операция
            else:
                res[i] += 1
    print(f'{index} \n{res[start_d:finish_d]}')  # вывел сверху делители для наглядности

    """
    Переменные:
    start, finish, start_d, finish_d, res, index, i, k 
    Теоретически 6 переменных int 
                 2 переменных List int, len = 9
    6 * 4 + 6 * 24 + 40 + (8 * len(res)) + 40 + (8 * len(index)) = >
    168 + 112 + 112 = 392
    """

    print()
    # Считаем память
    sum_mem = 0
    mem = 0
    for i in (start, finish, start_d, finish_d, res, index, i, k):
        mem = getsizeof(i)  # размер конкретной переменной
        sum_mem += mem
        print(f'{mem} + ', end='')
    print(f' = {sum_mem}')

    """
    Реально получается:
    28 + 28 + 28 + 28 + 184 + 184 + 28 + 28 +  = 536
    
    >>> sys.getsizeof([])
    56                      - получается пустой список занимает 56 бит
    >>> sys.getsizeof([2, 3, 4, 5, 6, 7, 8, 9, 10])
    128                     - в консоли выдаёт тоже 128
    >>> sys.getsizeof([10])
    64
    >>> sys.getsizeof([10, 10])
    72
    т.е. пустой список 56 бит, + 8 за каждый элемент
    для 9-ти элементов 56 + 8 * 9 = 128
    при выполнении программы выдаёт 184 разница в 56 бит
    где зарыта собака не знаю :-(
    """

    # Попробуем воспользоваться функцией deep_getsizeof из одной из статей (указана выше)

    print()
    # Считаем память deep_getsizeof
    sum_mem = 0
    mem = 0
    for i in (start, finish, start_d, finish_d, res, index, i, k):
        mem = deep_getsizeof(i, set())  # размер конкретной переменной
        sum_mem += mem
        print(f'{mem} + ', end='')
    print(f' = {sum_mem}')

    """
    Полученный результат:    
    28 + 28 + 28 + 28 + 404 + 436 + 28 + 28 +  = 1008
    т.к. функция берёт реальный размер данных, а не размер ссылки на данные, то получается объём ещё больше.
    тут вылазит специфика того, что питон оптимизирует часто встречающиеся данные. Например:
    "CPython управляет небольшими объектами (менее 256 байтов) в специальных пулах на 8-байтовых границах. 
    Есть пулы для 1-8 байтов, 9-16 байтов и вплоть до 249-256 байтов. Когда объект размером 10 выделяется, он 
    выделяется из 16-байтового пула для объектов размером 9-16 байт. Таким образом, хотя он содержит только 10 байтов
     данных, он будет стоить 16 байтов памяти."
    """


equation_of_a_straight_line(x1=7, y1=5, x2=1, y2=3)
print()
ascii_table()
print()
multiplicity()

print(f'Памяти для indeх {deep_getsizeof([2, 3, 4, 5, 6, 7, 8, 9, 10], set())}')