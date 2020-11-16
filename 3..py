import math
x=int(input("Введите значение x"))
X=int(input("Введите значение X"))


if x<=3:
    print("Первое значение", (math.pow(x, 2) - 3 * x + 9))
else:
    print("Введите значние меньше или равное трем")

if X>3:
    print("Второе значение", (1/(math.pow(X, 3) + 6)))
else:
    print("Введите значние больше трех")