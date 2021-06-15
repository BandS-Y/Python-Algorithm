#
import time


def three_to_sum_mul(a):
    """Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь"""

    b, c, d = [int(i) for i in str(a)]  # считаю, что к решению задачи этот цикл не относится
    print(f'Для числа {a}')
    print(f' сумма цифр = {b + c + d}')
    print(f' произведение цифр = {b * c * d}')


def bit_operations(a, b):
    """Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака."""

    print(f' в двоичном виде {a} =     {a:05b}')
    print(f' в двоичном виде {b} =     {b:05b}')
    print(f' побитовое И (AND) =     {(a & b):05b} или {a & b} в десятичном виде')
    print(f' побитовое ИЛИ (OR) =    {(a | b):05b} или {a | b} в десятичном виде')
    print(f' исключающее ИЛИ (XOR) = {(a ^ b):05b} или {a ^ b} в десятичном виде')
    print(f' побитовый сдвиг влево на два знака = {(a << 2):05b} или {a << 2} в десятичном виде')
    print(f' побитовый сдвиг впрво на два знака = {(a >> 2):05b} или {a >> 2} в десятичном виде')


def equation_of_a_straight_line(x1, y1, x2, y2):
    """По введенным пользователем координатам двух точек вывести уравнение прямой вида
        y = kx + b, проходящей через эти точки."""

    coefficient_a = y1 - y2
    coefficient_b = x1 - x2
    coefficient_c = x1 * y2 - x2 * y1
    print(f' Уравнение прямой для точек {x1, y1} и {x2, y2} выглядит \n следующим образом'
          f'  {coefficient_a}x + {coefficient_b}y + {coefficient_c} = 0')


def gen_random(begin=0, end=100, stage='i'):
    """Написать программу, которая генерирует в указанных пользователем границах
            случайное целое число,  (stage='i')
            случайное вещественное число, (stage='r')
            случайный символ. (stage='l')
    Для каждого из трех случаев пользователь задает свои границы диапазона.
    Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
    Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
    """

    seed_01 = str(time.time()).split('.')[1]
    time.sleep(0.000000000000001)
    seed_02 = str(time.time()).split('.')[1][::-1]
    seed_2 = seed_02 + seed_01
    seed = int(seed_2)
    seed ^= seed << int(seed_2[-6:-4]) + 1
    seed ^= seed >> int(seed_2[-9:-7]) + 1
    k = float('0.' + str(seed)[-16:-1])
    if stage == 'i':
        return int(begin + (end - begin + 1) * k)
    if stage == 'r':
        return begin + (end - begin + 1) * k
    if stage == 'l':
        begin = ord(begin) - 96
        end = ord(end) - 96
        return chr(int(begin + (end - begin + 1) * k) + 96)


def letter_between(a, b):
    """Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
     и сколько между ними находится букв."""

    pos_a = ord(a) - 96
    pos_b = ord(b) - 96
    len_in_alfabet = pos_b - pos_a - 1
    print(f'позиция первой буквы в алфавите= {pos_a}')
    print(f'позиция второй буквы в алфавите= {pos_b}')
    print(f'между ними находится букв {len_in_alfabet} ')


def letter_number(number):
    """Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

    print(f'это буква: {chr(number + 96)}')


def triangle_quest(a, b, c):
    """По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
    составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он
    разносторонним, равнобедренным или равносторонним."""

    if a + b > c and b + c > a and c + a > b:
        print(f'Треугольник со сторонами {a, b, c} существовать может')
        if a == b == c:
            print('Это равносторонний треугольник')
        elif a == b or b == c or c == a:
            print('это равнобедренный треугольник')
        else:
            print('Это разносторонний треугольник')
    else:
        print(f'Такого треугольника, со сторонами {a, b, c} не существует')


def leap_year(year):
    """Определить, является ли год, который ввел пользователем, високосным или не високосным."""

    if year % 4:
        print(f'{year} НЕ является високосным годом')
    elif not (year % 100):
        if not (year % 400):
            print(f'{year} является ВИСОКОСНЫМ годом')
        else:
            print(f'{year} НЕ является високосным годом')
    else:
        print(f'{year} является ВИСОКОСНЫМ годом')

    # Более короткая запись условия
    if year % 4 or (not (year % 100) and year % 400):
        print(f'{year} НЕ является високосным годом')
    else:
        print(f'{year} является ВИСОКОСНЫМ годом')


def midle_num(a, b, c):
    """Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""

    if a < b < c:
        print(f'cреднее число {b}')
    elif b < c < a:
        print(f'cреднее число {c}')
    else:
        print(f'cреднее число {a}')


print(help(three_to_sum_mul))
three_to_sum_mul(246)
print(" ")

print(help(bit_operations))
bit_operations(5, 6)
print(" ")

print(help(equation_of_a_straight_line))
equation_of_a_straight_line(x1=7, y1=5, x2=1, y2=3)
print(" ")

print(help(gen_random))
begin, end, stage = -100, 100, 'i'  # целые числа
print(f'Выводим случайные целые числа из промежутка {begin, end}:')
for i in range(50):
    # print(f' {gen_random_2(-50, 60)}', end='')
    print(f' {gen_random(begin, end, stage)}', end='')
begin, end, stage = -100, 100, 'r'  # вещественные числа
print(f'\n Выводим случайные вещественные числа из промежутка {begin, end}:')
for i in range(50):
    print(f' {gen_random(begin, end, stage)}', end='')
begin, end, stage = 'd', 'k', 'l'  # буквы
print(f'\n Выводим случайные буквы из промежутка {begin, end}:')
for i in range(50):
    print(f' {gen_random(begin, end, stage)}', end='')
print(" ")

print(help(letter_between))
letter_between('k', 'f')
print(" ")

print(help(letter_number))
letter_number(22)  # v
print(" ")

print(help(triangle_quest))
triangle_quest(5, 7, 6)  # Разносторонний треугольник
triangle_quest(5, 5, 5)  # Равносторонний треугольник
triangle_quest(12, 1, 5)  # Не возможжно собрать треугольник
triangle_quest(7, 8, 7)  # Равнобедренный треугольник
print(" ")

print(help(leap_year))
leap_year(2000)  # Високосный
leap_year(2004)  # Високосный
leap_year(2005)  # Обычный
leap_year(1000)  # Обычный
print(" ")

print(help(midle_num))
midle_num(1, 2, 3)
midle_num(2, 3, 1)
midle_num(3, 1, 2)
midle_num(2, 3, 3)
