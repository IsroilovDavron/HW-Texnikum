from dict import *
def sez(x):
    x = int(x)
    if x in zima:
        print('Это зимний месяц')
    elif x in vesna:
        print('Это весенний месяц')
    elif x in leto:
        print('Это летний месяц')
    elif x in osen:
        print('Это осенний месяц')
