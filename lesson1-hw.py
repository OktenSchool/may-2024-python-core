# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'as 23 fdfdg544'

# print(', '.join(num for num in st if num.isdigit()))


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fd22fd2g544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################
# st = 'as 23 fd22fd2g544 34'
# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))


# list comprehension
#
# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# print([ch.upper() for ch in greeting])

#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i**2 for i in range(50) if i%2])

# function
#
# - створити функцію яка виводить ліст
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def show_list(list_):
    for i in list_:
        print(i)

def show_max(a,b,c):
    res = max(a, b, c)
    print(res)
    return res

def min_max(*args):
    print(max(args))
    return min(args)

def max_from_list(list_):
    return max(list_)

def min_from_list(list_):
    return min(list_)

def sum_of_list(list_):
    return sum(list_)

def avg(list_):
    return sum(list_)/len(list_)

################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню
l = [22, 3,5,2,8,2,-23, 8,23,5]

def duplicate():
    copy = l.copy()
    print(list(set(copy)))

def to_x():
    copy = l.copy()
    print(['X' if not (i+1)%4 else item for i,item in enumerate(copy)])

# l = ['apple', 'pen', 'coffe']
#
# for i, v in enumerate(l):
#     print(i)
#     print(v)

def square(n):
    for i in range(n):
        if i ==0 or i == n-1:
            print('*'*n)
        else:
            print('*'+' '*(n-2)+'*')


def multi_table():
    size = 9
    i = 1
    while i <= size:
        j=1
        while j <= size:
            res = i*j
            # print(' ' if res//10 else '  ', end='')
            # print(res, end='')
            print(f'{res:3}', end='')
            j+=1
        print()
        i+=1


while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на "X"')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('9) вихід')

    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        print(min_from_list(l))
    elif choice == '2':
        duplicate()
    elif choice == '3':
        to_x()
    elif choice == '4':
        square(7)
    elif choice == '5':
        multi_table()
    elif choice == '9':
        break

