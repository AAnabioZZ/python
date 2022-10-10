# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

# import random
# def sumNeChot (li,chet):
#     sum =0
#     for i in range(chet,len(li)-1):
#         sum += int(li[i])
#     return sum
# 
# def newLst(size):
#     lst=[]
#     for i in range(size):
#         lst.append(round (random.uniform(1, 10),2))
#     return lst

# print(f"Привет, давай созданим массив и заполним его\nпотом я сосчитаю все четные или не четные элементы,\nкак захочешь)")
# size = int(input("Какого размера будем создавать массив?\nСколько элементов? : "))
# userList = newLst(size) 
# print (f"Вот нашь массив {userList}") 
# chet = int(input("Четние позиции будем складывать или нечетные?\nЕсли чет нажим 1\nЕсли нечет нажми 0\n : "))
# print(sumNeChot(userList,chet))

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def sumParList(lst):
#     sum=[]
#     for i in range(len(lst)-1):
#         if i <= len(lst)-1-i:
#             if i == len(lst)-1-i:
#                 sum.append(lst[i])
#             else:sum.append(lst[i]*lst[len(lst)-1-i])
#     return sum 

# lstik = [2, 2, 4, 8, 8]
# print(sumParList(lstik))

# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.

# def toBinar(num):
#     result=[]
#     while num !=0:
#         result.insert(0,num%2)
#         num //= 2 
#     return result

# a=int(input("Введите целочисленное значение, а мы преобразуем десятичное число в двоичное\n: "))
# print(*toBinar(a), sep="")


# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


# import random

# def newLst(size):
#     lst=[]
#     for i in range(size):
#         lst.append(round (random.uniform(1, 10),2))
#     return lst
# def maxMin(lst):
#     max=lst[0]%1
#     min=lst[0]%1
#     for i in lst:
#         if i%1 < min : min = round(i%1,2)
#         elif i%1 > max : max = round(i%1,2)
#     print(f"max :{max}\nmin :{min}\nDifference :{round(max-min,2)}")
# a=int(input("Введите размер листа:"))
# userList=newLst(a)
# print(userList)
# maxMin(userList)

# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def negafib(size):
#     lst=[1,0,1]
#     for i in range(size-1):
#         lst.insert(0,(lst[1]-lst[0]))
#     for i in range(size-1):
#         lst.append(lst[-1]+lst[-2])
#     print(lst)        

# negafib(int(input("Создадим последовательность Негафибаначи какого размара?: ")))
n = [47756688399943]

list = []
for i in n:
    list.append(n)
print(list)

# list_count = []
# for i in list:
#     count = 0
#     for k in list:
#         if k == i:
#             count += 1
#             list_count.append(count)
# print(list_count)

# result = []
# for i in range(len(list_count)):
#     if list_count[i] == 1:
#         result.append(list[i-1])
# print(result)