import math
a = int (input("Введите значение с клавиатуры"))
b = int (input("Введите значение с клавиатуры"))
c = int (input("Введите значение с клавиатуры"))
p = (a+ b+ c)/2
s = (p* (p- a)* (p- b)* (p- c))
r = (s/p)
print ("Площадь круга S = ",(math.pi * r* 2))