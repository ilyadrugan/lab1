import math
import sys

def getNumber (): 
    while True:
        print ('Введите число: ', end = '')
        getTempNumber=input ()
        try:
            getTempNumber=float(getTempNumber)
        except ValueError:
            print('"'+ getTempNumber + '"' + ' - не является числом')
        else:
            break
    return getTempNumber



if len(sys.argv) == 4:
    a = (sys.argv[1])
    b = (sys.argv[2])
    c = (sys.argv[3])
    print(a,b,c)
    while True:
        try:
            getTempNumberA = float(a)
            break
        except ValueError:
            print('Введенный коэффициент a не является числом')
            print('Введите число ')
            try:
                a = float(input("a = "))
            except ValueError:
                print("Не является числом")
                a = getNumber()
    while True:
        try:
            getTempNumberB = float(b)
            break
        except ValueError:
            print('Введенный коэффициент b не является числом')
            print('Введите число')
            try:
                b = float(input("b = "))
            except ValueError:
                print('Не является числом')
                b = getNumber()
    while True:
        try:
            getTempNumberC = float(c)
            break
        except ValueError:
            print('Введенный коэффициент c не является числом')
            print('Введите число')
            try:
                c = float(input("c = "))
            except ValueError:
                print('Не является числом')
                c = getNumber()

elif len(sys.argv) == 1:
    try:
        a = float(input("a = "))

    except ValueError:
        print("Не является числом")
        a = getNumber()
    
    try:
        b = float(input("b = "))
    except ValueError:
        print('Не является числом')
        b = getNumber()
    
    try:
        c = float(input("c = "))
    except ValueError:
        print('Не является числом')
        c = getNumber()
else:
    print("Неправильное количество параметров командной строки")
def f(a,b,c):
    result = []
    D = b * b - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        print("Корень уравнения: любое число")
    elif a == 0 and b == 0:
        print("Уравнение не имеет действительных корней")
    elif a == 0:
        preroot = -c/b
        if preroot > 0:
            print("x1 = {}, x2 = {}".format(math.sqrt(preroot), -math.sqrt(preroot)))
        elif preroot == 0: print("x1 = 0")


    else:
        if D == 0.0:
            preroot = -b / (2.0 * a)
            if preroot > 0:
                print("x1 = {}, x2 = {}".format(math.sqrt(preroot), -math.sqrt(preroot)))
            elif preroot == 0: print("x1 = 0")
        elif D > 0.0:
            sqD = math.sqrt(D)
            preroot1 = (-b + sqD) / (2.0 * a)
            preroot2 = (-b - sqD) / (2.0 * a)

            if preroot1 > 0:
                print("x1 = {}, x2 = {}".format(math.sqrt(preroot1), -math.sqrt(preroot1)))
            elif preroot1 == 0: print("x1 = 0")

            if preroot2 > 0:
                print("x3 = {}, x4 = {}".format(math.sqrt(preroot2), -math.sqrt(preroot2)))
            elif preroot2 == 0: print("x3 = 0")



print("a = {}, b = {}, c = {}".format(a, b, c))
a= float(a)
b= float(b)
c= float(c)
d = b ** 2 - 4 * a * c
f(a,b,c)
"""
if a == 0 and b == 0 and c == 0:
    print("Корень уравнения: любое число")
elif a == 0 and b == 0 and c != 0:
    print("Нет решений")
elif a == 0 and b != 0 and c == 0:
    print("x1 = 0")
elif a != 0 and b == 0 and c == 0:
    print("x1 = 0")
elif a == 0 and b != 0 and c != 0:
    print("x1 = 0")
elif a == 0 and b != 0 and c != 0:
    x = (-b / c)
    print("x1 = {}".format(x))
elif a != 0 and b != 0 and c == 0:
    x = (-b / a)
    print("x1 = 0 x2 = {}".format(x))
elif b == 0:
    x = (-b / c)
    print("x1 = {}".format(x))
elif d < 0:
    print("Уравнение не имеет действительных корней")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    if x1 < 0 and x2 < 0:
        print("Нет решений")
    elif x1 == x2:
        print("x1 = {}, x2 = {}".format(math.sqrt(x1), -math.sqrt(x2)))
    elif x1 < 0:
        print("x1 = {}, x2 = {}".format(math.sqrt(x2), -math.sqrt(x2)))
    elif x2 < 0:
        print("x1 = {}, x2 = {}".format(math.sqrt(x1), -math.sqrt(x1)))
    else:
        if x1 == 0:
            print("x1 = {}, x2 = {}, x3= {}".format(0, math.sqrt(x2), -math.sqrt(x2)))
        elif x2 == 0:
            print("x1 = {}, x2 = {}, x3= {}".format(0, math.sqrt(x1), -math.sqrt(x1)))
        else:
            print("x1 = {}, x2 = {}, x3 = {}, x4 = {}".format(math.sqrt(x1), -math.sqrt(x1), math.sqrt(x2), -math.sqrt(x2)))
"""
