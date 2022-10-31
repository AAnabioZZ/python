from check import chek

def add_hend():
    if not chek:
        with open('phone_book.csv', 'r+', encoding='utf-8') as phBook:
            phBook.write("Фамилия;Имя;Телефон;Комментарий\n")
    with open('phone_book.csv', 'r+', encoding='utf-8') as phBook:
        phBook.write(input("Введите Фамилию: ")+";")
        phBook.write(input("Введите Имя: ") + ";")
        phBook.write(input("Введите Телефон: ")+";")
        phBook.write(input("Введите Описание: "))
        phBook.write("\n")
    return print("\nГотова!👍\n\nДанные внесены👌\n") 
    