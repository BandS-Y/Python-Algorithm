from timeit import timeit
import random
from math import log1p


def max_count(count_my=10000, start=0, finish=100000):
    """4. Определить, какое число в массиве встречается чаще всего."""

    array_internal = [random.randint(start, finish) for _ in range(count_my)]  # Заполняем массив
    res = [0 for _ in range(finish + 1)]
    max_unit, pos_unit = 0, 0
    for i in array_internal:  # Записываем в массив результатов
        res[i] += 1
    for i in range(len(res)):  # Считаем мксимально встречающееся число
        if max_unit < res[i]:
            max_unit = res[i]



# print(timeit('max_count()', setup='from __main__ import max_count', number=10))

# Сложность алгоритма O(2n)
# Такая сложность идёт от того, что максимум мы можем сгенерировать полный массив не повторяющихся значений,
# тогда первый проход по множеству даст количесво повторений в целевом массиве, а второй проход даст максимальное
# из массива индексов повторений т.е. 2n
# т.к. фактически сложность не большаи и линейная, то время выполнения очень маленькое, даже при больших числах
#

def prime_number_force(n=2000):
    pn_list = []  # писок простых чисел, который будем заполнять по мере нахождения
    s = 1
    # k = 0  # для подсчёта количества циклов
    while len(pn_list) < n:
        for i in range(2, s + 1):
            # k += 1  #
            if not (s % i) and s == i:
                pn_list.append(s)
                break
            if not (s % i):
                break
        s += 1
    # print(k)
    # print(pn_list[n - 1])


def prime_number_erat(n):  # n - каое по счёту простое число хотим найти
    n1 = int(n * log1p(n) * 1.2)  # оцениваем придел до которого необходимо дойти
    s = list(range(n1 + 1))  # заполняем список
    # k = 0  # для подсчёта количества циклов
    s[1] = 0  # убираем единицу
    for i in s:
        if i > 1:
            for j in range(i + i, len(s), i):
                # k += 1
                s[j] = 0
    s1 = [x for x in s if x != 0]
    # print(k)
    # print(s1[n - 1])

# Сложность первого алгоритма О(n(n+1)/2), но реально меньше, т.к. половина циклов по чётным числам сразу отбрасывается
# для n = 2000 получается 16 356 662 циклов, а расчётная асимптотическая  151 188 660.
# Для второго алгоритма сложность составляет О(n log(log n)) или 43 456 для n = 2000. Что на 4 порядка меньше.
#
#Находим 500-е число прямым перебором. Время работы составляет:  1.0913929409999998
# Находим 500-е число решетом Время работы составляет:  0.009081318000000005
# Находим 1000-е число прямым перебором. Время работы составляет:  4.831639176
# Находим 1000-е число решетом Время работы составляет:  0.022447446999999343
# Находим 1500-е число прямым перебором. Время работы составляет:  11.415601989999999
# Находим 1500-е число решетом Время работы составляет:  0.034113445999999215
# Находим 2000-е число прямым перебором. Время работы составляет:  21.451610125000002
# Находим 2000-е число решетом Время работы составляет:  0.048650842999997224
#
# Видно, что время выполнения значительно отличается.

# for i in (4, 25, 168, 1229, 9592, 78498):
#     print(eratosthenes(i))  # где n - любое число
# print(prime_number_erat(2000))

for i in range(500, 2001, 500):
# i = 2000
    print(f'Находим {i}-е число прямым перебором. Время работы составляет: ',
          timeit(f"prime_number_force({i})", setup='from __main__ import prime_number_force', number=10))
    print(f'Находим {i}-е число решетом Время работы составляет: ',
          timeit(f"prime_number_erat({i})", setup='from __main__ import prime_number_erat', number=10))

#
# prime_number_force()
# max_count()