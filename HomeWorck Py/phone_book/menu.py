from ctypes.wintypes import INT
from  check import  *
#from reed import reed_all

def choi(a:int):
    return menu(chek_int(input("Выбор: ")),0,a)
def start():
    print(f"Привет✌, добро пожаловать в телефонный справочник\n📖📞\n1. Записать 🖊\n2. Прочитать👀\n0. Выход🚪")
    choice = choi(2)
    if choice == 1:
        return menu_add()
    elif choice == 2:
        return 

    else: exit()

def menu_add():
    print(f"Как будем добавлять?\n📖📞\n1. Из файла 📖\n2. В ручную 🖊\n0. Вернутся🚪")
    choice = choi(2)
    if choice == 1:
        menu_add()
        return menu_finish()
        
    elif choice == 2:
        return 
    else: return start()

def menu_finish():
    print(f"На этом все или еще что нибудь?\n📖📞\n1. Еще 📖\n0. Выход🚪")
    choice = choi(1)
    if choice:
        return start()
    else: return exit()

def menu_reed():
    print(f"Поищем когото конкретного или посмотрим все?\n📖📞\n1. Поиск 📖\n2. Вывести все. 🖊\n0. На главную🚪")
    choice = choi(2)
    if choice == 1:
        #menu_faind()
        return menu_finish()
    elif choice == 2:
        return reed_all()
    else: return start()
    
#def menu_faind():
#    print(f"Как искать будем??\n📖📞\n1. По имяни? 📖\n2. По фамилии? 🖊\n3. По телефону? 🖊\n0. На главную🚪")
#    choice = choi(3)
#    if choice == 1:
#        find_name()
start()