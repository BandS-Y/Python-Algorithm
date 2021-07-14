import itertools as it
import hashlib

"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, 
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""


# возвращает все подстроки строки из нужного количества символов
def substring(in_str, n):  # Написал свою функцию, т.к. в tertools нет необходимого инструмента
    out_str = []
    for i in range(len(in_str) - n + 1):
        out_str.append(in_str[i:i + n])
    return out_str


def all_substring(in_str):  # возвращает все подстроки всех длинн, кроме нулевой и самой строки
    out_str = []
    for i in range(1, len(in_str)):
        out_str.append(substring(in_str, i))
    return out_str


def hash_table(in_list):  # Делаем полную таблицу по подстрокам, хешам, и результатам совпадений хешей
    count_internal = 0
    res_table = []
    for in_substr_list in in_list:  # перебираем списки с подстроками разной длинны
        for in_substr in in_substr_list:  # перебираем подстроки одинаковой длинны
            count_internal += 1
            h = hashlib.sha1(in_substr.encode('utf-8')).hexdigest()  # вычисляем хеш подстроки
            h_in = h in [res_table[i][2] for i in range(len(res_table))]  # проверяем, есть ли такой хэш в таблице
            res_table.append([count_internal, in_substr, h, h_in])  # добавляем результат в таблицу
    return res_table


def hash_def_internal(in_list):  # возвращаем количество оригинальных подстрок
    res_list = []
    for in_substr_list in in_list:  # всё как в функции выше
        for in_substr in in_substr_list:
            h = hashlib.sha1(in_substr.encode('utf-8')).hexdigest()
            if h not in res_list:  # проверяем наличие хэша в таблице
                res_list.append(h)
    return len(res_list)


my_string = 'alldklifjpekloriff'  # задаём строку для проверки
# print(substring(my_string, 4))  # для тестирования работы функции
# print(all_substring(my_string))  # для тестирования работы функции
res = hash_table(all_substring(my_string))  # получаем таблицу всех результатов
res_1 = hash_def_internal(all_substring(my_string))  # получаем количество оригинальных подстрок через хэш

for i in res:  # вывод полной таблицы
    print(i)

for i in range(len(res)):  # вывод  только совпадающих значений
    if res[i][3]:
        print(res[i])

print(f'количество оригинальных подстрок в строке = {res_1}')  # вывод количества оригинальных подстрок

# a = list(it.combinations(my_string, 2))  # это для проверки itertools
# print(a)  # здесь видно, что перебор не верен выводятся все возможные комбинации


""" ________________________________________________________________________________

2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

____________________________________________________________________________________
"""

my_string = "sldjfaoiefrf asogijoirgfv nfauerfbnzzefiadjcvn"  # строка, которую будем кодировать
haf_dict = {}  # Полученный словарь

class Node(object):  # класс узела
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


class HuffmanTree(object):  # Строим дерево
    def __init__(self, char_weights):
        self.Leaf = [Node(k, v) for k, v in char_weights.items()]  # создаём список узлов
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node: node.value, reverse=True)  # отсортируем по возрастанию частоты вхождения
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))  # оздаём узел с двумя потомками
            n.left = self.Leaf.pop(-1)
            n.right = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def gen_dict(self, node, len_branch):  # оздадим словарь
        global haf_dict  # глобальный словарь Хафмана для входящей строки
        code = ''
        if not node:
            return
        elif node.name:
            for i in range(len_branch):  # обходим ветки для генерации кода
                code += str(self.Buffer[i])  # собираем значение кода
            haf_dict.update({node.name: code})  # добавляем в словарик
            return
        self.Buffer[len_branch] = 0
        self.gen_dict(node.left, len_branch + 1)
        self.Buffer[len_branch] = 1
        self.gen_dict(node.right, len_branch + 1)

    def get_code(self):  # инииализируем создание словаря
        self.gen_dict(self.root, 0)


def friq_dict(my_string):  # Создаём частотный словарь строки
    res_dict = {}  # выходной частотный словарь
    for i in my_string:
        if i in res_dict:  # для символа в словаре
            res_dict[i] += 1  # увеличиваем счётчик
        else:
            res_dict.update({i: 1})  # создаём запись в словаре, если нет такого знака
    return res_dict

def coding_str(my_string):  # кодируем строку по словарю
    out_str = ''
    for i in my_string:
        out_str = "".join(haf_dict[char] for char in my_string)
    return out_str


def huffman_decode(in_coding_str):  # функция декодирования исходной строки
    global haf_dict
    out_str =[]  # раскодированная строка
    enc_ch = ""  # раскодированный символ
    for ch in in_coding_str:  # обойдем закодированную строку по символам
        enc_ch += ch  # добавим текущий символ к строке закодированного символа
        for dec_ch in haf_dict:  # ищем закодированный символ в словаре кодов
            if haf_dict.get(dec_ch) == enc_ch:  # если закодированный символ найден,
                out_str.append(dec_ch)  # добавим значение раскодированного символа к массиву раскодированной строки
                enc_ch = ""
                break
    return "".join(out_str)


print(f'Исходная строка : {my_string}')
HuffmanTree(friq_dict(my_string)).get_code()  # получаем частотный словарь, строим дерево и создаём словарь
print(f'получили словарь: {haf_dict}')
coding_string = coding_str(my_string)  # кодируем строку
print(f'получаем закодированную строку: {coding_string}')
decoding_string = huffman_decode(coding_string)  # декодируем строку
print(f'получаем декодированную строку: {decoding_string}')
print(f'Проверяем исходную и раскодированную строку на совпадение: {my_string == decoding_string}')

# print(tree.Leaf)

