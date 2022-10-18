
print(f"Привет✌, добро пожаловать в телефонный справочник\n📖📞\n1. Записать 🖊\n2. Прочитать👀\n0. Выход🚪")
choice = int(input("Выбор: "))
while choice > 0:
    if choice == 1 :
        with open('phone_book.csv', 'r+', encoding='utf-8') as phBook:
            lines=0
            for line in phBook:
                lines+=1
            if lines < 1:
                phBook.write("Фамилия;Имя;Телефон;Комментарий\n")
            phBook.write(input("Введите Фамилию: ")+";")
            phBook.write(input("Введите Имя: ") + ";")
            phBook.write(input("Введите Телефон: ")+";")
            phBook.write(input("Введите Описание: "))
            phBook.write("\n")
            print("\nГотова!👍\n\nДанные внесены👌\n")      
    elif choice == 2:
        with open('phone_book.csv', 'r', encoding='utf-8') as phBook:
            while True:
                line = phBook.read()
                if not line: break
                print(line)
    print(f"Попробуем еще?\n     📖📞\n1. Записать 🖊\n2. Прочитать👀\n0. Выход🚪")
    choice = int(input("Выбор: "))
print("До скорой встречи✌")