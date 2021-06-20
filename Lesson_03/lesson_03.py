import random


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
    return f'{index} \n{res[start_d:finish_d]}'  # вывел сверху делители для наглядности


def index_even(in_array):
    """2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
     со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
     (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива
     стоят четные числа."""

    out_array = []
    for i in range(len(in_array)):
        if in_array[i] % 2:
            pass
        else:
            out_array.append(i)
    return out_array


def find_min_max_pos(count_my=20, start=0, finish=100):  # Сделал входные параметры для универсальности
    """3.1 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы"""

    array_internal = [random.randint(start, finish) for _ in range(count_my)]  # Заполняем массив
    max_unit, min_unit, pos_max_unit, pos_min_unit = start, finish, 0, 0
    for i in range(count_my):
        if array_internal[i] > max_unit:  # Ищем максимальный элемент
            max_unit = array_internal[i]
            pos_max_unit = i
        elif array_internal[i] < min_unit:  # Ищем минимальный элемент
            min_unit = array_internal[i]
            pos_min_unit = i
    return max_unit, min_unit, pos_max_unit, pos_min_unit, array_internal


def change_max_min():
    """3.2 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
    Здесь меняем элементы найденные в функции поиска максимальных и минимальных элементов"""

    count_my = 20
    finish = 100
    max_unit, min_unit, pos_max_unit, pos_min_unit, array_internal = find_min_max_pos(count_my=count_my, start=0,
                                                                                      finish=finish)
    # Оформляем вывод данных
    print(f'{max_unit = } {pos_max_unit = } \n{min_unit = } {pos_min_unit = }')
    print('   num index', end='')
    for i in range(count_my):
        print(f'{" " * (len(str(finish)) - len(str(i)))}  {i}', end='')  # Автоматическая подстройка размера
    print('\n start array', end='')
    for i in array_internal:
        print('%5d' % i, end='')  # Другой, менее универсальный вариант, не будет работать на больших числах
    array_internal[pos_max_unit] = min_unit
    array_internal[pos_min_unit] = max_unit
    print('\nresult array', end='')
    for i in array_internal:
        print(f'{" " * (len(str(finish)) - len(str(i)))}  {i}', end='')


def max_count(count_my=100, start=0, finish=10):
    """4. Определить, какое число в массиве встречается чаще всего."""

    array_internal = [random.randint(start, finish) for _ in range(count_my)]  # Заполняем массив
    res = [0 for _ in range(finish + 1)]
    max_unit, pos_unit = 0, 0
    for i in array_internal:
        res[i] += 1
    for i in range(len(res)):
        if max_unit < res[i]:
            max_unit = res[i]
            pos_unit = i
    print(f'максимальное количество раз {max_unit} встречается значение {pos_unit}')


def gen_list(k=20, range_internal=10):  # Генерируем список
    n = []
    for _ in range(k + 1):
        n.append(int((random.random() * range_internal + 1) - range_internal / 2))
    return n


def max_negativ(array):
    """5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""

    array_neg = []  # массив отрицательных элементов
    array_pos = []  # массив позиций
    for i in range(len(array)):
        if array[i] < 0:
            array_neg.append(array[i])  # добавляем отрицательный элемент
            array_pos.append(i)  # добавляем позицию отрицательного элемента

    max_neg = array_neg[0]
    pos = array_pos[0]
    for i in range(len(array_neg)):
        if array_neg[i] > max_neg:  # ищем максимальный элемент из массива отрицательных элементов
            max_neg = array_neg[i]  # максимальный элемент
            pos = array_pos[i]  # позиция максимального элемента в исходном массиве
    print(f'исходный массив: {array}')
    print(f'максимальный элемен из отрицательных = {max_neg} находится на позиции {pos}')


def sum_beetwin(count_my=20, start=0, finish=100):
    """6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
     Сами минимальный и максимальный элементы в сумму не включать."""

    # Воспользумся функцией из задачи 3

    max_unit, min_unit, pos_max_unit, pos_min_unit, array_internal = find_min_max_pos(count_my=count_my, start=start,
                                                                                      finish=finish)
    sum_beetwin_my = 0
    # Выводим первую часть таблицы, как в задаче 3, можно было выделить в отдельную функцию, но должны же быть
    # хоть какие-то недостатки в коде :-)
    print(f'{max_unit = } {pos_max_unit = } \n{min_unit = } {pos_min_unit = }')
    print('   num index', end='')
    for i in range(count_my):
        print(f'{" " * (len(str(finish)) - len(str(i)))}  {i}', end='')  # Автоматическая подстройка размера
    print('\n start array', end='')
    for i in array_internal:
        print('%5d' % i, end='')  # Другой, менее универсальный вариант, не будет работать на больших числах
    print('\n')

    if pos_max_unit < pos_min_unit:  # мотрим, позиции, чтоб правильно взять срез
        pos_max_unit, pos_min_unit = pos_min_unit, pos_max_unit  # Переворачиваем позиции, если расположение обратное
    print(f'Элементы между наибольшим и наименьшим:')
    print(array_internal[pos_min_unit + 1:pos_max_unit])
    for i in array_internal[pos_min_unit + 1:pos_max_unit]:  # Считаем сумму между элементами
        sum_beetwin_my += i
    print(f'\n Сумма элементов между наибольшим и наименьшим числом = {sum_beetwin_my}')


def find_double_min(count_my=20, start=0, finish=50):  # Сделал входные параметры для универсальности
    """7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
    между собой (оба являться минимальными), так и различаться."""

    array_internal = [random.randint(start, finish) for _ in range(count_my)]  # Заполняем массив
    min_1_unit, min_2_unit, pos_min_1_unit, pos_min_2_unit = finish, finish, 0, 0
    for i in range(count_my):
        if array_internal[i] < min_1_unit:  # Ищем минимальный элемент
            min_2_unit = min_1_unit  # Перемещаем первый эл. на второе место
            min_1_unit = array_internal[i]  # Записываем минимальный элемент на первое место
            pos_min_2_unit = pos_min_1_unit
            pos_min_1_unit = i
        elif array_internal[i] < min_2_unit:  # Ищем второй по величине элемент
            min_2_unit = array_internal[i]
            pos_min_2_unit = i
    # Вывод организован подобно предыдущим задачам
    print(f'{min_1_unit = } {pos_min_1_unit = } \n{min_2_unit = } {pos_min_2_unit = }')
    print('   num index', end='')
    for i in range(count_my):
        print(f'{" " * (len(str(finish)) - len(str(i)))}  {i}', end='')
    print('\n       array', end='')
    for i in array_internal:
        print(f'{" " * (len(str(finish)) - len(str(i)))}  {i}', end='')


def matrix_input():  # Вообще можно заполнить матрицу любой размерности
    """8.1 Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. """

    print('Введите строки матрицы по очереди. для выхода наберите ни чего не набирайте')
    input_line = [' ']
    input_matrix = []
    while input_line:  # Пока не введём пустую строку или любой символ
        input_line = [int(i) for i in input("Введите строку матрицы: ").split() if str.isdigit(i)]
        input_matrix.append(input_line)
    input_matrix.pop()
    return input_matrix


def matrix_line_sum(matrix):  # Функция подсчитает сумму по строке
    """8.2 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
    В конце следует вывести полученную матрицу."""

    for i in range(len(matrix)):  # Считаем сумму по строе
        sum_line = 0
        for j in range(len(matrix[i])):
            sum_line += matrix[i][j]
        matrix[i].append(sum_line)

    print('    matrix    sum line')  # Заголовок таблицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:  # Ищем последний элемент строки
                print('  ' + '%5d' % matrix[i][j], end='')  # печатаем последний элемент строки
            else:
                print('%3d' % matrix[i][j], end='')  # печатаем основную строку
        print()


def max_from_min(matrix):
    """9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

    matrix.append([i for i in (matrix[0])])  # Добавляем последнюю строку
    for i in range(len(matrix[0])):  # Длинна строки или количество столбцов
        for j in range(len(matrix) - 1):  # Количество строк, кроме послкдней
            if matrix[len(matrix) - 1][i] > matrix[j][i]:  # Ищем минимальный элемент в столбце матрицы,
                matrix[len(matrix) - 1][i] = matrix[j][i]  # кроме последней строки. И помещаем в последнюю строку
    max_in_rows = 0
    for i in range(len(matrix[0])-1):
        if max_in_rows < matrix[-1][i]:  # Ищем максимальный элемент по последней строке
            max_in_rows = matrix[-1][i]
    # Вывод результатов
    print('    matrix')  # Заголовок таблицы
    for i in range(len(matrix)):
        if i < len(matrix)-1:
            for j in range(len(matrix[i])):
                print('%3d' % matrix[i][j], end='')  # печатаем основные строки
        else:  # Печать строки с минимальными элементами по столбцам
            for j in range(len(matrix[i])):
                print('---', end='')
            print('--')
            for j in range(len(matrix[i])):
                print('%3d' % matrix[i][j], end='')
        print()
    print(f'\nМаксимальный элемент из минимальных по столбцам = {max_in_rows}')


# print(multiplicity())
# print(index_even([0, 1, 9, 3, 8, 4, 5, 7, 1, 0, 4, 5, 9, 0, 9, 8, 3, 4, 5, 1]))
#
# change_max_min()
# max_count()
#
#
# print(gen_list(20))
# max_negativ(gen_list(20))
# sum_beetwin()

# find_double_min()

# print(matrix_input()) # Ввод матрицы вручную
#
# matrix_line_sum([[1, 2, 3, 5], [1, 3, 4, 6], [4, 3, 1, 7], [5, 8, 2, 9]])
# matrix_line_sum(matrix_input())  # То же самое, что и предыдущее, только с ручным вводом
#
# max_from_min([[1, 1, 10, 10, 8], [1, 5, 3, 4, 6], [4, 3, 9, 10, 7], [5, 8, 2, 9, 5]])
