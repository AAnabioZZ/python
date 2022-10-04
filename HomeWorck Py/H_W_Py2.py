# 1) 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр..

# a= float(input("Введите вещественное число а мы посчитаем сумму чисел в нем: "))
# result=0
# while a%1 != 0:
#     a*=10
# while a!=0:
#     result=result + (a%10)
#     a=a//10
# print(a)

# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# f=int(input("давайте посчитаем факториал, какого числа будем считать? :"))
# result=1
# for i in range(1,f+1):
#     result *=i
#     print(result, end ="|")


# 3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.

# Пример:

# Для n = 5: сумма = 11,55

# n=int(input("введите чесло целое число n: "))
# res=0
# lst=[]
# for i in range(1,n+1):
#     lst.append(round((1+ (1/n))**n, 2))
# for i in lst:
#     res += i
# print(res)
# print(lst)


# 4**) Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from fileinput import close

lst=[]
lst2 =[]
resalt =1
n=int(input("Введите число n: "))
for i in range(-n,n):
    lst.append(i)

t = open('D:\\MyPrograms\\Python\HomeWorck Py\\text.txt')
for line in t:
        lst2.append(int(line))
close

for i in lst2:
    resalt *= lst[i-1]

print(f"Позиции в файле: {lst2}")
print(f"Нашь список: {lst}")
print(f"Результат перемножения: {resalt}")

# 5**) Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)

# import time
# import datetime

# a = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
# for i in range(len(a)-1):
#     tempi = datetime.datetime.now().microsecond % len(a)
#     time.sleep(0.003)
#     # print(tempi)
#     temp = a[tempi]
#     a[tempi] = a[i]
#     a[i] = temp
# print(a)
