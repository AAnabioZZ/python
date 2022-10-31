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
def menu(a:int,min:int,max:int)->int:
    while not min-1<a<max+1:
        a=chek_int(input(f'Вне диапазона выбора, введите от {min} до {max}:'))


