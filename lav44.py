a = int(input('Введите число: '))
if (a % 3  == 0):
    print('Число делится на три')
else:
    print('Число не делится на три')

def lab2():
    try:
        a = int(input('Число: '))
    except ValueError:
        print('Строка, неправильные данные')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    else:
        print(a / 100)

lab2()

def lab3():



lab3()



