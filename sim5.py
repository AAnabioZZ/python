
# from random import choice

# def fill_list(count: int):
#     my_list = [x for x in range(count + 1)]
#     my_list.remove(choice(my_list))
#     return my_list

# new_list = (fill_list(int(input('Write count: '))))
# print(new_list)

# def find(my_list: list):
#     for i in range(1, len(my_list)):
#         if my_list[i] - 1 != my_list[i-1]:
#             return my_list[i] - 1
#     return -1

# print(find(new_list))

# # ??????????????????????
# def newList(size):
#     lis = [x+1 for x in size]
#     lis.remove(choice(lis))
#     return lis


# print(newList(int(input("Введите число"))))

# 2. Дан список чисел. Создайте список, в который попадают числа,
#    описываемые возрастающую последовательность.
#    Порядок элементов менять нельзя.

# from random import choice, choices


# def newLst(size):
#     lst = choices(range(1, size * 2), k=size)
#     return lst


# Listik = newLst(int(input()))


# def range_nums(ls):
#     new_Lis = []
#     for i in range(ls):
#         f = ls[i]
#         ls1 = [f]
#         for j in range(i+1, len(ls)-1):
#             if ls[j] > f:



