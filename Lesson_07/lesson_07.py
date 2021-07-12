import random

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на 
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована 
в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""


def bubble_sort_0(in_list):
    out_list = in_list.copy()  # Делаем копию, чтоб не менять исходный массив
    n = 1
    count_comparing = 0
    for i in range(len(in_list)):  # Пробегаемся по всем парам массива
        for k in range(len(in_list)-n):  # Пробегаемся по парам до отсортированных
            if out_list[k] > out_list[k + 1]:
                out_list[k], out_list[k + 1] = out_list[k + 1], out_list[k]  # Если певый больше второго меняе местами
            count_comparing += 1
            # print(f'{k=} {i=} {out_list}')  # Вывод для отладки
        n += 1
    print(out_list)
    print('количество проходов для bubble_sort_0 =  {0:,}'.format(count_comparing).replace(',', ' '))
    return out_list

"""
Улучшения:
1. Сделаем проверку на то, что при каком либо проходе перестановок не было. Значит список уже отсортирован
2. Запомним индекс первого обмена с начала строки, и будем начинать обмены с него т.о. уменьшим количество проверок.

Сравним количество проверок для обоих алгоритмов
"""


def bubble_sort_1(in_list): # Здесь реализован флаг отсортированного массива
    out_list = in_list.copy()  # Делаем копию, чтоб не менять исходный массив
    n = 1
    flag = True
    count_comparing = 0
    while flag:
        flag = False
        for k in range(len(in_list)-n):  # Пробегаемся по парам до отсортированных
            if out_list[k] > out_list[k + 1]:
                out_list[k], out_list[k + 1] = out_list[k + 1], out_list[k]  # Если певый больше второго меняе местами
                flag = True
            # print(f'{k=} {i=} {out_list}')  # Вывод для отладки
            count_comparing += 1
        n += 1
    # print(out_list)
    print('количество проходов для bubble_sort_1 =  {0:,}'.format(count_comparing).replace(',', ' '))
    return out_list


def bubble_sort_2(in_list):  # здесь реализован алгоритм фиксации уже отсортированных пар
    out_list = in_list.copy()  # Делаем копию, чтоб не менять исходный массив
    n = 1
    count_comparing = 0
    point_not_change = 0
    for i in range(len(in_list)):  # Пробегаемся по всем парам массива
        flag_not_change = True
        for k in range(point_not_change, len(in_list)-n):  # Пробегаемся по парам до отсортированных
            if out_list[k] > out_list[k + 1]:
                if flag_not_change:  # Проверяем былали сделана перестановка
                    flag_not_change = False
                    if point_not_change + k - 1 > 0:  # если перестановка была сделана не вначале то
                        point_not_change = k - 1  # Запоминаем место перестановки
                out_list[k], out_list[k + 1] = out_list[k + 1], out_list[k]
                # Если певый больше второго меняе местами с учётом смещения
            count_comparing += 1
            # print(f'{k=} {i=} pnc={point_not_change} fnc={flag_not_change} {out_list}')  # Вывод для отладки
        n += 1
    # print(out_list)
    print('количество проходов для bubble_sort_2 =  {0:,}'.format(count_comparing).replace(',', ' '))
    return out_list


def bubble_sort_3(in_list):  # овмещаем 2 и 3 усовершенствования
    out_list = in_list.copy()  # Делаем копию, чтоб не менять исходный массив
    n = 1
    point_not_change = 0
    flag = True
    count_comparing = 0
    while flag:
        flag = False
        flag_not_change = True
        for k in range(point_not_change, len(in_list)-n):  # Пробегаемся по парам до отсортированных
            if out_list[k] > out_list[k + 1]:
                if flag_not_change:
                    flag_not_change = False
                    if point_not_change + k - 1 > 0:
                        point_not_change = k - 1
                out_list[k], out_list[k + 1] = out_list[k + 1], out_list[k]
                flag = True
                # Если певый больше второго меняе местами с учётом смещения
            count_comparing += 1
            # print(f'{k=} {i=} pnc={point_not_change} fnc={flag_not_change} {out_list}')  # Вывод для отладки
        n += 1
    # print(out_list)
    print('количество проходов для bubble_sort_3 =  {0:,}'.format(count_comparing).replace(',', ' '))
    return out_list


"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на 
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""


def merge(left_list, right_list):
    global count_merge_iter
    out_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):  # Пробегаемся по всем элементам
        count_merge_iter += 1
        # проверяем, что не достигли концов списков
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:  # сравниваем левые элементы списков
                out_list.append(left_list[left_list_index])  # добавляем если левый меньше правого
                left_list_index += 1
            else:
                out_list.append(right_list[right_list_index])  # добавляем если правый меньше левого
                right_list_index += 1
        elif left_list_index == left_list_length:  # если левый список кончился
            out_list.append(right_list[right_list_index])  # добавляем правый оставшийся список
            right_list_index += 1
        elif right_list_index == right_list_length:  # если правый кончился
            out_list.append(left_list[left_list_index])  # добавляем левый оставшийся список
            left_list_index += 1
    # print(out_list) # для отладки
    return out_list


def merge_sort(in_list):
    if len(in_list) <= 1: # Проверяем, что список больше 1 элемнета
        return in_list
    mid = len(in_list) // 2  # Находим середину списка
    left_list = merge_sort(in_list[:mid])  # Рекурсивно сортируем части списков
    right_list = merge_sort(in_list[mid:])
    return merge(left_list, right_list)  # Возвращаем объединение отсортированных списков

def median_find(l):
    if len(l) % 2 == 1:  # если длинна списка чётная передаём в работу половину списка
        return find_in(l, len(l) / 2)
    else:  # если чётное берём среднее
        return 0.5 * (find_in(l, len(l) / 2 - 1) + find_in(l, len(l) / 2))


def find_in(l, k):
    if len(l) == 1:  # проверяем, что дошли до одног элемента и возвращаем его
        return l[0]
    pivot = random.choice(l)  # выбираем случайный элемент в половине
    lows = [el for el in l if el < pivot]  # выбираем всё, что меньше ключевого элемента
    highs = [el for el in l if el > pivot]  # выбираем всё, что больше ключевого элемента
    pivots = [el for el in l if el == pivot]  # ключевой элемнет
    if k < len(lows):  # если меньших чисел больше
        return find_in(lows, k)  # ищем медиану там
    elif k < len(lows) + len(pivots):  # здесь мы попали на медиану
        return pivots[0]
    else:
        return find_in(highs, k - len(lows) - len(pivots))  # ищем медиану в большем списке


count_merge_iter = 0  # счётчик итерацй для merge
len_sort_list = 16  # длинна генерируемого списка

# in_list = [random.randint(-101, 100) for _ in range(len_sort_list)]  # Генерируем массив
# print(in_list)
# # # при выводе проверяем правильность результата за счёт сравнения результатов всех фукций
# print(f'Совпадают ли результаты сортировок '
#       f'{bubble_sort_0(in_list) == bubble_sort_1(in_list) == bubble_sort_2(in_list) == bubble_sort_3(in_list) == merge_sort(in_list)}')
#
# # Немного поменяем условие задачи (по входящему списку), чтоб сравнить работу обоих алгоритмов
# print('количество проходов для merge_sort    =  {0:,}'.format(count_merge_iter).replace(',', ' '))

in_list = [random.randint(-999, 1000) for _ in range(2 * len_sort_list + 1)]  # Генерируем массив 2 * len_sort_list + 1
print(in_list)

# вывод результата с нумерацией элементов, чтоб легче искать было
for i in range(2 * len_sort_list + 1):
    print(' %-4d' % i, end="")
print()
num = merge_sort(in_list)
for i in num:
    print('%-4d ' % i, end="")
print()
print(f'длинна списка {len(in_list)}')
print(merge_sort(in_list)[len(in_list) // 2])  # выводим медианный элемент отсортированного списка
print(median_find(in_list))