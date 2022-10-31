
if not chek():
    with open("phone_book.csv") as file:
        print([row.strip() for row in file])