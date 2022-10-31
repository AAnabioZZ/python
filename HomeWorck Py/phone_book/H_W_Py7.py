def chek():
    try:
        with open('phone_book.csv', 'r+', encoding='utf-8') as phBook:
            return True
    except:
        return False
def chek_int(a:str)->int:
    try:
        int(a)
        return int(a)
    except:
        return chek_int(input('ой, это не число, попробуй еще:'))


print(f"Привет✌, добро пожаловать в телефонный справочник\n📖📞\n1. Записать 🖊\n2. Прочитать👀\n0. Выход🚪")
choice = chek_int(input("Выбор: "))
while choice > 0:
    if choice == 1 :
        if not chek:
            with open('phone_book.csv', 'r+', encoding='utf-8') as phBook:
                phBook.write("Фамилия;Имя;Телефон;Комментарий\n")
        with open('phone_book.csv', 'r+', encoding='utf-8') as phBook:
            phBook.write(input("Введите Фамилию: ")+";")
            phBook.write(input("Введите Имя: ") + ";")
            phBook.write(input("Введите Телефон: ")+";")
            phBook.write(input("Введите Описание: "))
            phBook.write("\n")
            print("\nГотова!👍\n\nДанные внесены👌\n")      
    elif choice == 2:
        if chek():
            with open('phone_book.csv', 'r', encoding='utf-8') as phBook:
                while True:
                    line = phBook.read()
                    if not line: break
                    print(line)
        print('Увы, но файла пока нет. Создайте новые записи чтобы фаил появился.')
    print(f"Попробуем еще?\n     📖📞\n1. Записать 🖊\n2. Прочитать👀\n0. Выход🚪")
    choice = chek_int(input("Выбор: "))
print("До скорой встречи✌")