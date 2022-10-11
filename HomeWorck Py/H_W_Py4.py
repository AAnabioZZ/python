# # 1. Вычислить число c заданной точностью d

# a = float(input("Введите натуральное число: "))
# b = input("Введите требуемую точность, например '0.00001': ")
# print(f'{a:.{len(b)-2}f}')




# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = 180
# def prostMnozh(nam):
#     ls=[]
#     d=2
#     while d <= nam :
#         if nam%d==0:
#             ls.append(d)
#             nam/=d
#             d= 1
#         d+=1        
#     return ls

# print(prostMnozh(n))

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.
# import random
# def newLst(size):
#     lst=[]
#     for i in range(size):
#         lst.append(random.randint(1, 10))
#     return lst

# lst1 = newLst(5)   
# print(lst1) 
# for i in lst1:
#     if lst1.count(i) < 2:
#         print(i, end=" ")

# Задана натуральная степень k. Сформировать случайным образом
#  список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.

import random 
def znak():
    if random.getrandbits(1) : return "+"
    else: return "-"
h = int(input("Введите положительную степень: "))
if h > 0:
    with open('Mnogochlen1.txt', 'w', encoding='utf-8') as mnog1:
        for _ in range(3):
            k=h
            while k > 0:
                ran= random.choice(range(0,h))
                if ran > 1:
                 mnog1.write(f'{ran}*x^{k} {znak()} ')
                k -=1
            else : mnog1.write(f'{ran} = 0\n')
else: 
   with open('Mnogochlen1.txt', 'a', encoding='utf-8') as mnog1:
     mnog1.write(f'от {h} не могу создать последовательность')
