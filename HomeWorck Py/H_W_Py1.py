# 1    Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# a = int(input("Ведите номер для недели от 1 до 7 : "))
# if a < 6 and a > 0:
#     print("это будний день")
# elif a > 5 and a < 8:
#     print ("это выходной")
# else:
#     print ("Хей мы же просили цифру от 1 до 7 !?")

# 2  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f"{(x,y,z)} {not(x or y or z) == (not x and not y and not z)}", end = "|")

# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# a = 0
# while (a==0):
#     x = int(input("Ведите x должен быть целое число и не 0! : "))
#     y = int(input("Ведите y должен быть целое число и не 0! : "))
#     if x == 0 or y == 0:
#         print("Ой, где то закрался 0, попробуем еще разок!")
#     else:
#         break

# if x > 0 and y > 0:
#     print(f"{x,y} относится к 1 четверти 2х мерной координатной сетки")
# if x < 0 and y > 0:
#     print(f"{x,y} относится к 2 четверти 2х мерной координатной сетки")
# if x < 0 and y < 0:
#     print(f"{x,y} относится к 3 четверти 2х мерной координатной сетки")
# if x > 0 and y < 0:
#     print(f"{x,y} относится к 4 четверти 2х мерной координатной сетки")

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input("Введите номер четверти 2х мерной координатной сетки: "))

# if a == 1:
#     print("1 четверть вкючает в себя 'x' > 0 и 'y' > 0")
# elif a == 2:
#     print("2 четверть вкючает в себя 'x' < 0 и 'y' > 0")
# elif a == 3:
#     print("3 четверть вкючает в себя 'x' < 0 и 'y' < 0")
# elif a == 4:
#     print("4 четверть вкючает в себя 'x' > 0 и 'y' < 0")
# else:
#     print("Ввели число не отражающие номер четверти. Перезапустите программу и попробуйте еще раз.")

# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# print("введите координаты точки а: ")
# a1 = int(input("Ax ="))
# a2 = int(input("Ay ="))
# print("введите координаты точки b: ")
# b1 = int(input("Bx ="))
# b2 = int(input("By ="))
# result = (((a1-b1)**2)+((b2-a2)**2))**0.5
# print(round(result, 3))

