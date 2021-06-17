import random


def calc_my():
    """1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
    Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
    а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе
    символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
    то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о
    невозможности деления на ноль, если он ввел 0 в качестве делителя."""

    operation = '+'
    while operation:
        a, b = [int(i) for i in input("введите два числа для вычислений: ").split()]
        operation = input("введите операцию  (+, -, *, /) для вычисления или 0 для завершения: ")
        if b == 0 and operation == '/':
            print('На ноль делить нельзя!')
            continue
        while operation not in ['0', '+', '-', '*', '/']:
            operation = input(
                "Ошибка ввода операции! \n введите операцию  (+, -, *, /) для вычисления или 0 для завершения: ")
        else:
            if operation == '0':
                operation = int(operation)
                print('Завершаем программу.')
            elif operation == '+':
                print(f'{a + b = }')
            elif operation == '-':
                print(f'{a - b = }')
            elif operation == '*':
                print(f'{a * b = }')
            elif operation == '/':
                print(f'{a / b = }')


def count_digit(n):
    """2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
    то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

    even_my = []
    not_even_my = []
    count_even_my, count_not_even_my = 0, 0

    for i in range(len(n)):
        if int(n[i]) % 2:
            not_even_my.append(n[i])
            count_not_even_my += 1
        else:
            even_my.append(n[i])
            count_even_my += 1

    print(f'В числе {n}')
    print(f'{count_even_my} чётых чисел {even_my}')
    print(f'{count_not_even_my} не чётых чисел {not_even_my}')


def revers_digit(n):
    """3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
     Например, если введено число 3486, то надо вывести число 6843."""

    reversed_digit = []
    for i in range(len(n) - 1, -1, -1):
        reversed_digit.append(n[i])
    print(f"Для числа {n} обратный порядок цифр выглядит так: \n          {''.join(reversed_digit)}")


def up_sum(n):
    """4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    Количество элементов (n) вводится с клавиатуры."""

    global s
    s = 1

    def sum_of_element(n):
        global s
        if n <= 1:
            return 1
        s += sum_of_element(n - 1) * -0.5
        return sum_of_element(n - 1) * -0.5

    sum_of_element(n)
    return s


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


def guess_the_number(begin=0, end=100, tray=10):
    """6. В программе генерируется случайное целое число от 0 до 100.
    Пользователь должен его отгадать не более чем за 10 попыток.
    После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
    чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число."""

    print(f"Привет! Я загадал число от {begin} до {end}. Попробуй угадать его. У тебя {tray} попыток. \n Поехали!")
    hidden_number = random.randint(begin, end)
    # print(hidden_number)
    user_num = -1
    user_tray = 0

    while user_num != hidden_number and user_tray < tray:
        user_tray += 1
        user_num = int(input("Введите число: "))
        if user_num == hidden_number:
            print(f'Вы угадали! Я загадал число {hidden_number}. \n Вам понадобилось {user_tray} попыток.')
        elif user_num > hidden_number:
            print(f'Загаданное число меньше вашего. Попробуйте ещё раз. У вас {tray - user_tray} попыток.')
        else:
            print(f'Загаданное число больше вашего. Попробуйте ещё раз. У вас {tray - user_tray} попыток.')
    if user_tray >= tray:
        print('Вы исчерпали все свои попытки. \n Игра закончена.')

def proof_func(n):
    """7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
    равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число."""

    def n_func(n):
        if n == 1:
            return 1
        return n + n_func(n-1)
    formula = (n * (n + 1)) / 2
    return f'Для {n = } формула {n_func(n) == formula}'


def count_digit(input_digit):  # цифра, которую ищем и число в котором ищем
    """8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
    Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

    i = 0
    for a in range(len(input_digit[0])):
        if input_digit[0][a] == input_digit[1]:
            i += 1
    return f'цифра {input_digit[1]} встречается {i} раз в числе {input_digit[0]}'

def max_sum_num(num_in):
    """9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
     Вывести на экран это число и сумму его цифр."""

    max_sum, max_num = 0, 0  # Максимальные сумма и число
    for i in range(len(num_in)):  # пробегаемся по чилам присланным нам
        now_sum = 0  # Вычисляемая сумма числа, которое мы обрабатываем
        for k in range(len(num_in[i])):  # Пробегаемся по цифрам суммируемого числа
            now_sum += int(num_in[i][k])  # вычисляем сумму числа
        if now_sum >= max_sum:  # проверяем является ли сумма наибольшей
            max_sum = now_sum  # если является, то текущую сумму записываем в максимальную
            max_num = num_in[i]  # текущее число записываем в максимальное по сумме
    return f'Максимальная сумма {max_sum} в числе {max_num}'


# calc_my()

# count_digit('2454587499375027308')
# count_digit(input("Введите число для подсчёта в нём чётных и нечётных цифр: "))

# revers_digit('0013567890800')
# revers_digit(input('Введите число для того, чтоб увидеть реверсное к нему: '))

# print(up_sum(5))
# print(f'Сумма элементов членов последовательности = {up_sum(int(input("Введите количество
# элементов последовательности: ")))}')

# ascii_table()

# guess_the_number()

# print(proof_func(10))
# print(f'{proof_func(int(input("Введите количество элементов для проверки формулы: ")))}')

# print(count_digit(['40193571409501934163498345723095017263594871634587', '5']))
# print(f'{count_digit(input("введите число в котором будем искать цифру и саму цифру: ").split())}')

# print(max_sum_num(['23423', '35656', '32542', '45677']))
# print(max_sum_num(input("введите числа среди которых будем искать максимальное по сумме цифр: ").split()))