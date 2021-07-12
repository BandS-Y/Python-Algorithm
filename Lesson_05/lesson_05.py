import decimal
from collections import namedtuple
import random

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.


# Создадим namedtuple для данных о фирме
# На мой взгляд он здесь не нужен, но задание...

firm_data = namedtuple('Firm', 'name_firm quarter_y_1 quarter_y_2 quarter_y_3 quarter_y_4 sum_y middle_y')
firm_data_in = [0 for _ in range(7)]  # заполняем массив
firm_base = []  # данные по всем фмрмам


def input_data_manual():  # Ввод данных вручную
    firm_data_in[0] = input("Введите название предприятия: ")
    firm_data_in[1:5] = [int(i) for i in input("введите значения дохода поквартально (четыре числа): ").split()]
    firm_data_in[5] = sum(i for i in firm_data_in[1:5])
    firm_data_in[6] = firm_data_in[5] / 4
    print(firm_data_in)
    firm_base.append(firm_data._make(firm_data_in))  # На эту строку убил кучу времени,
                                                     # точнее на нахождение метода _make


def input_data_auto(num):  # Генерация данных автоматически
    firm_data_in[0] = f'Firm_{num}'
    firm_data_in[1:5] = [random.randint(30, 100) for _ in range(4)]
    firm_data_in[5] = sum(i for i in firm_data_in[1:5])
    firm_data_in[6] = firm_data_in[5] / 4
    firm_base.append(firm_data._make(firm_data_in))


def average_income(firm_count):  # Расчёт среднего по году для всех фирм
    sum_inc, ave_inc = 0, 0
    for i in range(firm_count):
        sum_inc += firm_base[i].sum_y
    ave_inc = sum_inc / firm_count
    return ave_inc


def range_of_income(firm_count):  # Создание рейтинга фирм отностительно среднего по году и печать
    firm_up_ave = []  #
    firm_under_ave = []  #
    for i in range(firm_count):
        if firm_base[i].sum_y >= ave_inc:
            firm_up_ave.append(firm_base[i].name_firm)
        else:
            firm_under_ave.append(firm_base[i].name_firm)
    print("Фирмы доход которых выше среднего дохода фирм по году:")
    for i in range(len(firm_up_ave)):
        print(f'{firm_up_ave[i]}')
    print('-' * 40)
    print("Фирмы доход которых выше среднего дохода фирм по году:")
    for i in range(len(firm_under_ave)):
        print(f'{firm_under_ave[i]}')
    print('-' * 40)


# n = int(input("Ведите количество предприятий "))  # Запрос количества фирм
n = 5  # Запись количества фирм для автоматизации

# for i in range(n):  # запрашиваем данные по фирмам
#     input_data_auto(i)  # автоматическое заполнение
#     # input_data_manual()  # ручное заполнение
# ave_inc = average_income(n)  # рассчёт среднего по году
# range_of_income(n)  # ранжировка фирм
# print(f'Средний доход составляет {ave_inc}')
# for i in range(n):
#     print(f'Доход фирмы {firm_base[i].name_firm} за год составил {firm_base[i].sum_y}')

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и
# C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# список для конвертации чисел из 10 в 16
compliance = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def convert_10(num):  # Конвертор из 16 в 10
    in_num = list(num)
    in_num.reverse()
    in_num_10 = 0
    for i in range(len(num)):
        in_num_10 += compliance.index(in_num[i]) * 16 ** i
    return in_num_10


def convert_16(num):  # Конвертор из 10 в 16
    in_num_16 = []
    while num > 0:
        in_num_16.append(compliance[num % 16])
        num //= 16
    in_num_16.reverse()
    return ''.join(in_num_16)


def input_number():  # Запрашиваем числа и проводим над ними операции
    in_num_1 = input("Ведите первое шестнадцатеричное число: ")
    in_num_2 = input("Ведите второе шестнадцатеричное число: ")
    operation = input("Ведите операцию '+' или '*': ")
    dec_num_1 = convert_10(in_num_1)
    dec_num_2 = convert_10(in_num_2)
    if operation == '+':
        print(f'Результат операции равен: {convert_16(dec_num_2 + dec_num_1)}')
    elif operation == '*':
        print(f'Результат операции равен: {convert_16(dec_num_2 * dec_num_1)}')
    else:
        print("я не смогу выполнить такую операцию")


# in_num_1 = 'a2'
# in_num_2 = 'c4f'

input_number()