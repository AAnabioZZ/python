# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# from random import choices,random,sample

# def abc(cur: int):
#     stroka = ""
#     bcc = ["а","б","в"]
#     for i in range(cur):
#         stroka = stroka + "".join(sample(bcc,3)) + " "
#     return stroka

# def find_end_del(str: str,delit: str):
#     list=str.split()
#     # print(list)
#     while True:
#         try:
#             list.remove(delit)
#         except:
#             break
#     return " ".join(list)

# size=int(input("Number of words: "))
# if size > 0 :
#     abc_list = abc(size)
#     print(abc_list)
#     print(find_end_del(abc_list,"абв"))
# else:
# print('The data is incorrect')


# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q
# def on_arhiv(st: str):
#     temp = ''
#     st2 = ''
#     for i in arhi:
#         if i.isdigit():
#             if temp == '':
#                 temp = i
#             else:
#                 temp += i
#         else:
#             st2 += i*int(temp)
#             temp = ''
#     return (st2)


# def in_arhiv(st: str):
#     st2 = ''
#     temp = ''
#     count = 0
#     for i in st:
#         if temp != '':
#             if i != temp:
#                 st2 += str(count) + temp
#                 temp = i
#                 count = 1
#             else:
#                 count += 1
#         else:
#             temp = i
#             count = 1
#     return st2


# st = "aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa"
# print("input: "+st)
# print('zip: ' + in_arhiv(st))
# print('on zip: ' + on_arhiv(in_arhiv(st)))

# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# Эмодзи
# def check_int(st:str)->int:
#     try:
#         int(st)
#         if int(st) >0<10:
#             return int(st)
#         else: return check_int(input('Ошибка ввода, попробуйте снова: '))
#     except:
#         return check_int(input('Ошибка ввода, попробуйте снова: '))

# def convert_to_index(a:int)->int:
#     if a == 1:
#         return 2
#     elif a == 2:
#         return 8
#     elif a == 3:
#         return 14
#     elif a == 4:
#         return 38
#     elif a == 5:
#         return 44
#     elif a == 6:
#         return 50
#     elif a == 7:
#         return 74
#     elif a == 8:
#         return 80
#     elif a == 9:
#         return 86
#     else:
#         return convert_to_index(check_int(input('Некорректный ввод\n'
#                                       'Введите номер свободной ячейки: ')))

# def hodd(pol: str,hod: int, play: str) -> str:
#     if pol[hod] != '❌' and pol[hod] != '⭕':
#         pol = pol[:hod]+play+pol[hod+1:]
#     else:
#         hod=convert_to_index(check_int(input('Эта ячейка занято повторите выбор:')))
#         return hodd(pol,hod,play)
#     return pol

# def winer(pol:str):
#     p1,p2,p3,p4,p5,p6,p7,p8,p9=2,8,14,38,44,50,74,80,86
#     if pol[p1] == pol[p2] ==pol[p3]:
#         return True
#     elif pol[p4] == pol[p5] ==pol[p6]:
#         return True
#     elif pol[p7] == pol[p8] ==pol[p9]:
#         return True
#     elif pol[p1] == pol[p4] ==pol[p7]:
#         return True
#     elif pol[p2] == pol[p5] ==pol[p8]:
#         return True
#     elif pol[p3] == pol[p6] ==pol[p9]:
#         return True
#     elif pol[p1] == pol[p5] ==pol[p9]:
#         return True
#     elif pol[p3] == pol[p5] ==pol[p7]:
#         return True
#     else: return False

# def chei_hod(count_hod:int):
#     if count_hod %2 == 0 :
#         return '❌'
#     else: return '⭕'

# polosa='-----------------'
# pole= '  1  |  2  |  3  \n'+polosa+'\n  4  |  5  |  6  \n'+polosa+'\n  7  |  8  |  9  '
# count=0
# win=False
# print('\n'*20+f'Привет сиграем в крестики нолики ?\nТебе понадобится апонент так что ищи друга')
# print('Приступим')

# while not win and count<9:
#     print(pole)
#     play=chei_hod(count)
#     shag=convert_to_index(check_int(input(f'Cейчас ходит{play}\nКуда ставим{play}?: ')))
#     pole=hodd(pole,shag,play)
#     win=winer(pole)
#     count+=1
#     print('\n'*20)

# if win:
#     print(f'Спустя {count} ходов,\nпобедил {chei_hod(count-1)} поздравляем!\n\n{pole}')
#     input("для выхода нажмити Ввод ")
# else:
#     print(f'{pole}\n!Победила дружба!')
#     input("для выхода нажмити Ввод ")


# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
import random


def check_int(st: str, min: int, max: int) -> int:
    try:
        int(st)
        if (min-1) < int(st) < (max+1):
            return int(st)
        else:
            return check_int(input('Ошибка ввода, попробуйте снова: '), min, max)
    except:
        return check_int(input('Ошибка ввода, попробуйте снова: '), min, max)

def check_imp(inp:int,imp:int)->int:
    if inp>imp:
        return check_int(input(f'ой, а столько нету, осталось {imp}: '), 1, imp)
    else: return inp

def bot(x: int) -> int:
    if x % 29:
        return x % 29
    else:
        return random.randint(1, 28)


konfet = 100


print('\n'*20+f'Привет сыгрем в конфеты?\nПравила просты у нас есть {konfet}шт конфет,'
      ' берем конфеты по очереди,\nколичеством от 1 до 28шт. Кто взял последнюю тот проиграл)!\nПогнали!')

vibor = check_int(
    input('Играем с другом или с ботом?\n1. с другом\n2. с ботом\n'), 1, 2)
if vibor == 1:
    play = 1
    while konfet > 0:
        if play == 3:
            play = 1
        a = check_imp(check_int(
            (input(f'осталось {konfet} конфет, ходит игрок {play} : ')), 1, 28),konfet)
        if konfet-a == 0:
            break
        print(f'{konfet} конфет - {a} конфет остается {konfet-a}')
        konfet = konfet - a
        play += 1
    print(f'победил игрок {play}')
    input("для выхода нажмити Ввод ")
else:
    while konfet > 0:
        print(konfet % 29)
        a = check_imp(check_int((input(f'осталось {konfet} конфет, твой ход: ')), 1, 28),konfet)
        if konfet-a == 0:
            print('конец! победил игрок!')
            input("для выхода нажмити Ввод ")
            exit()
        print(f'{konfet} конфет - {a} конфет остается {konfet-a}'
              '\nходит бот\n'
              f'{konfet-a} конфет - {bot(konfet-a)} конфет остается {konfet-a-bot(konfet-a)}')
        konfet = konfet-a-bot(konfet-a)
    print('конец, победил бот.')
    input("для выхода нажмити Ввод ")
