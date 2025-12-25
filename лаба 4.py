#задание 4 и 1
import math, datetime as dt
a = int(input("Введите число"))
print(math.sqrt(a))
print(dt.datetime.now().time())

#задание 4 и 2

import mymodule as cd


print(cd.factorial(5))
print(cd.hello())
#3 задание
import packet.file1 as file1
import packet.file2 as file2

a = int(input("Введите число"))
print(file1.prostnumb(a))

b = int(input("Ввелите кол-во эл в списке"))
spisok = []
for i in range(0,b):
    dop = int(input("Введите число"))
    spisok.append(dop)
print(file2.revers(spisok))
