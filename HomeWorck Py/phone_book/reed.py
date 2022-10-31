from check import chek

def reed_all():
    if chek():
            with open('phone_book.csv', 'r', encoding='utf-8') as phBook:
                while True:
                    line = phBook.read()
                    if not line: break
                    return print(line)
    return print('Увы, но файла пока нет. Создайте новые записи чтобы фаил появился.')