import math
a=int(input("Введите сторону"))
b=int(input("Введите сторону"))
c=int(input("Введите сторону"))
d=int(input("Введите сторону"))
A=int(input("Введите угол"))
B=int(input("Введите угол"))
C=int(input("Введите угол"))
D=int(input("Введите угол"))

if (a==b==c==d) and (A==B==C==D):
    print("Квадрат")
else:
    if (a==b==c==d) and (A==C) and (B==D):
        print("Ромб")
    else:
        if (a==c) and (b==d) and (A==B==C==D):
            print("Прямоугольник")
        else:
            if (a==c) and (b==d) and (A==C) and (B==D):
                print("Параллелограмм")