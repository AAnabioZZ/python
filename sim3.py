# a = "привет, мир привет, друзья"
# b = "привет"
# c = a.split(" ")
# count = 0
# print(c)

# for i in c:
#     if i == b:
#         count += 1
# print(count)

# str1 = 'привет, мир, привет, коллеги, привет друзья'
# str2 = 'привет'
# print(str1.count(str2))

# import datetime
# print(datetime.datetime.now().microsecond % 12)

# text1 = ["привет","аваа","вапап 7 ап ","ваорло"]
# def find_digit(text, nam):
#     for i in range(len(text)):
#         for j in text[i]:
#             if j.isdigit():
#                 if j == nam:
#                     print(i)
# find_digit(text1, 7)

str1 = ["привет", "мир", "мир", "привет", "коллеги", "привет", "друзья"]
fin = "привет"
count=0
for i in range(len(str1)):
    if str1[i] == fin:
        count +=1
    if count == 2:
       count=i
       break
if count < 2 :
    print(-1)
else:
    print(count)
