baza={'name':['Davron', 'Farhod', 'Petr', 'Nargiza', 'Katerina'],
      'age':[31, 29, 30, 18, 15],
      'sex':['M', 'M', 'M', 'F', 'F']}

def gap0():
    print('''\nВыберите пункт для выполнение действий
1. Просмотр базы клиентов
2. Добавить нового клиента
3. Удалить клиента из базы
4. Редактировать данные клиента
5. Очистить базу клиентов''')


def gap1():
    print('Список всех клиентов')
    a = 0
    while a<len(baza['name']):
        print(str(a+1)+'.', baza.get('name')[a], baza.get('age')[a], baza.get('sex')[a])
        a = a + 1

def gap2():
    print('Введите данные клиента')
    n=input('Введите имя: ')
    y=input('Введите возраст: ')
    s=input('Введите пол: ')
    print('Новый клиент записан:',n,y,s)
    baza.get('name').append(n)
    baza.get('age').append(y)
    baza.get('sex').append(s)

def gap3():
    x=int(input('Введите номер клиента:'))
    baza.get('name').pop(x-1)
    baza.get('age').pop(x-1)
    baza.get('sex').pop(x-1)
    print('Клиент удален из базы!!!')
def gap4():
    print('Введите номер клинета')
    a=int(input())
    a=a-1
    print(baza.get('name')[a], baza.get('age')[a], baza.get('sex')[a])
    print('Внесите изменения')
    baza.get('name')[a]=input('Введите новое имя: ')
    baza.get('age')[a]=input('Введите новый возраст: ')
    baza.get('sex')[a]=input('Введите новый пол: ')

def gap5():
    baza.clear()
    print('Клиетская база очищена!!!')
