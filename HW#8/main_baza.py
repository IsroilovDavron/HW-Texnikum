from Const_Func import *
x='a'
while x!='stop':
    gap0()
    x = input()
    if x=='1':
        gap1()
    elif x=='2':
        gap2()
    elif x=='3':
        gap3()
    elif x=='4':
        gap4()
    elif x=='5':
        gap5()
    elif x=='6':
        k=input('''Выберите параметр
        1. По порядковому номеру
        2. По имени\n''')
        if k=='1':
            gap61()
        elif k=='2':
            gap62()
        else:
            print('Неккоректное значение')

    else:
        print('Неккоректное значение')







