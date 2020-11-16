year = int(input("Введите год"))
month = int(input("Введите месяц"))

if month <=7:
    print ("Первое полугодие")
else:
    print("Второе полугодие")

if month in (1, 2, 3):
    print("Первый квартал")
else:
    if month in (4, 5, 6):
        print("Второй квартал")
    else:
        if month in (7, 8, 9):
            print("Третий квартал")
        else:
            if month in (10, 11, 12):
                print("Четвертый квартал")

if month in (11, 1, 2):
    print("Зима")
else:
    if month in (3, 4, 5):
        print("Весна")
    else:
        if month in (6, 7, 8):
            print("Лето")
        else:
            if month in (9, 10, 11):
                print("Осень")
if year < 100:
    print("1 век")
else:
    print( f'{year // 100 + 1} век')

if year < 1000:
    print("1 тысячелетие")
else:
    print(f'{year // 1000 + 1} тысячелетие')

if (not year % 4 and year % 100) or (not year % 100 and not year % 400):
    print("Високосный год")
else:
    print("Не високосный год")








