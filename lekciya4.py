# lis=[1,2,3,5,8,15,23,38]
# lis2=[(i,i**2) for i in lis if i %2 == 0]
# print(lis2)

from unicodedata import digit


def f(g,j):
    return [g(i) for i in j if i.isdigit()]

data = "3 4 5 6 7 8 9 kj 45 34 56".split()
print(type(data[7]))
yps = f(int,data)
print(yps)