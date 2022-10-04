# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

def sumNeChot (li,chet):
    sum =0
    for i in range(chet,len(li)-1):
        sum += int(li[i])
    return sum
def USList(siz):
    lst = []
    for i in range(siz):
        lst.append(int(input(f"Введите {i+1}е число: ")))   
    return lst

print(f"Привет, давай созданим массив и заполним его\n потом я сосчитаю все четные или не четные элементы,\n как захочешь)")
size = int(input("Какого размера будем создавать массив?\nСколько элементов? : "))
userList = USList(size) 
print (f"И вот нашь массив {userList}") 
chet = int(input("Чет будем складывать или нечет?\nЕсли чет нажим 1\nЕсли нечет нажми 0\n : "))
print(sumNeChot(userList,chet))
