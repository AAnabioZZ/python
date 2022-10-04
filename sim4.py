

# line = input()
# list_1 = [int(x.strip(',.*')) for x in line.split() if x.replace('-','').isdigit()]
# print(f'Mix: {min(list_1)}')
# print(f'Max: {max(list_1)}')


# from math import sqrt
# def sqr_r(a, b, c):
#     if a == 0 :
#         return print("а - не может быть 0")
#     else: 

#         d = b ** 2 - 4 * a * c
#         with open('sqr.txt', 'a', encoding='utf-8') as my_f:
#             my_f.write(f"{a}x**2 + {b}x + {c} = 0\n")
#             if d > 0:
#                 my_f.write(f'{(-b + sqrt(d)/(2*a))}\n')
#                 my_f.write(f'{(-b - sqrt(d)/(2*a))}\n')
#             elif d == 0:
#                 my_f.write(f'{-b /(2*a)}\n')
#             else:
#                 my_f.write('Нет корней\n')


# for i in range(3):
#     sqr_r(int(input("a: ")), int(input("b: ")), int(input("c: ")))
from math import gcd
a=int(input("a= "))
b=int(input("b= "))
print(a*b//gcd(a,b))
print(gcd(a,b))



