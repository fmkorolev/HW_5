#  Задание 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более 
# чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

CANDIES_ON_TABLE = 2021
# CANDIES_ON_TABLE = 121    # testing value
AMT_MAX = 28
names = tuple()
mode = ''

def game_play() -> None:
    """basic logic"""
    global names
    candies = CANDIES_ON_TABLE
    person = randint(0, 1)
    flag = 1
    while flag:
        print(f'Конфет на столе: {candies}')
        if mode == '1':
            if person:
                num_take = human(person)
                if num_take > 28 or num_take < 0:
                    num_take = AMT_MAX
            else:
                num_take = ai_player(candies)
        else:
            num_take = human(person)
            if num_take > 28 or num_take < 0:
                num_take = AMT_MAX

        if candies <= 28:
            print(f'{names[person]} забирает {candies} конфет.')
        else:
            print(f'{names[person]} берёт {num_take} конфет.')
        candies -= num_take
        if candies <= 0:
            print(f'{names[person]} победил')
            flag = 0
        person = (person + 1) % 2


def ai_player(candies: int) -> int:
    """primitive AI"""
    if candies < 28:
        return candies
    elif candies - 28 > 1 and candies < 28 * 2:
        return candies - 27
    else:
        return 28


def human(pers: int) -> int:
    """human capture"""
    global names
    return int(input(f'Сколько конфет берёте (0 min, 28 max), {names[pers]}? '))


def intro():
    print(
        '''
        Играем в конфеты. 
        Полиси: можно взять от 0 до 28 штук.
        Если взять меньше 0 (интересный вариант...) или больше 28,
        считается что взял 28. Поехали.    
    '''
        )

    flag_0 = 1
    global mode
    global names
    while flag_0:
        mode = input('Играем с компьютером или на двоих? (1/2/exit): ')
        if mode == 'exit':
            print('Выход')
            raise SystemExit
        elif mode not in ('1', '2'):
            print('Ошибка ввода.')
        else:
            flag_0 = 0

    if mode == '1':
        names = ('An artificial one', input('Введите имя: '))
    else:
        names = (input('Введите имя 1-го игрока: '), input('Введите имя 2-го игрока: '))

    game_play()


intro()

#  Задача 1- Напишите программу, удаляющую из текста все слова, 
#  содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

a = [w.lower() for w in input('Enter text : ').split()]
sample  = input('Введите шаблон для удаления :').lower()
for i in range(len(a)-1, -1, -1):
    if a[i].find(sample) != -1:
        del a[i]
print(' '.join(a))

#  Задача 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]

from functools import reduce
def create_tuples(values, ind):
    return list(zip(ind, values))


def filtr(array):
    for i in range(len(array)-1, -1, -1):
        num = []
        for c in array[i][1]:
            num.append(ord(c))
        if sum(num) % array[i][0] == 0:
            lang = array[i][1].upper()
            del array[i]
            array.insert(i, (reduce(lambda x,y: x + y, num), lang))
        else:
            del array[i]
    return array


lan = ['python', 'c#', 'kobol', 'pascal', 'c++', 'assembler',
       'r', 'java', 'go', 'fortran', 'scratch', 'php', "swift"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
my_tup = create_tuples(lan, num)
print(my_tup)
res = filtr(my_tup)
print(res)

def Encode(string):
    result = ""
    count = 1
    for i in range(len(string)):
        letter = string[i]
        if i != len(string) - 1:
            if string[i + 1] == letter:
                count += 1
            else:
                result += letter + str(count)
                count = 1
        else:
            result += letter + str(count)
            count = 1
    return result

def Decode(string):
    result = ""
    i = 0
    while i < len(string):
        main_letter = string[i]
        str_num = ""
        count = 1
        while string[i + count].isnumeric() and i + count < len(string):
            str_num += string[i + count]
            count += 1
            if i + count >= len(string):
                break
        i += count
        for j in range(int(str_num)):
            result += main_letter
    return result

with open("text1.txt", 'r') as data:
    inpt_string = data.read()

print(f"Исходная строка:\r\n{inpt_string}")

outpt_string = Encode(inpt_string)
print(f"Вот что из этого вышло:\r\n{outpt_string}")

with open("text2.txt", 'w') as data:
    data.writelines(outpt_string)

with open("text2.txt", 'r') as data:
    inpt_string = data.read()

print(f"Прочитано из файла: \r\n{inpt_string}")

outpt_string = Decode(inpt_string)

print(f"Вот что из этого вышло:\r\n{outpt_string}")