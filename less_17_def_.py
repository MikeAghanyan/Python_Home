# import lib

# print(lib.tri())


# x = {2, 3, 5, 7, 34,2 ,5,10 }
# print(x)
# ------------------------------------------
'''slide-CALCULATOR'''
# from lib import calculator
# print(calculator(5, 5, '*'))

# ------------------------------------------------------
'''To find max of two numbers'''
# print(max(int(input('Enter a number ---> ')), int(input('Enter a number ---> '))))

# ------------------------------------------------------
'''SUM'''
# def summary(*x) -> float:
#     a = 0
#     while x != 0:
#         x = float(input('Enter a number ---> '))
#         a += x
#     return a
# print(summary())

# ------------------------------------------------------
'''MULTIPLY ??? kak umnozit' na 0.5??? i vvodit' float(*x)  ''' 

# def multiply(*x) -> int:
#     a = 1
#     while x != '':
#         x = input('Enter a number ---> ')
#         if x == '':
#             return a
#         elif x.isdigit():
#             a *= int(x)
# print(multiply())

# ------------------------------------------------------
# '''SUM ALL LETTERS AND NUMBERS'''
# def allsumm(text = input('Enter the numbers and the letters ---> ')) -> str:
#     a = 0
#     b = '' # esli otdel'no to []
#     for i in text:
#         if i.isalpha():
#             b += i
#             # b.append(i)
#         elif i.isdigit():
#             a += int(i)
#     return f'{b} is all used letters \n{a} is summmary of all used numbers'
# print(allsumm())

# ------------------------------------------------------
'''PASSANGERS'''
# def passangers(a = int(input('Enter the first passanger age ---> ')), b = int(input('Enter the second passanger age ---> ')), c = int(input('Enter the third passanger age ---> '))):
#     mylist = [a, b, c]
#     count = 0
#     while count < 3:
#         for j in mylist:
#             if j < 17:
#                 count += 3
#                 return 'TOO young'
#             else:
#                 count += 1
#     if count == 3:
#         return 'get ready!'
# print(passangers())
# 
#
# age = input('Enter the passangers age with space ---> ')): 
#     age = age.split(' ')
#     for i in age:
#         if i.isdigit():
#             if int(i) < 17:
#                 return 'TOO YOUNG!'
#             else:
#                 return 'Get ready!'
#         else:
#             return 'Enter the age, please!'
# print(passangers())

 
    # while x >= 17:
    #     mylist.append(x)
    # return mylist


# age = input('Enter the passangers age with space ---> ')
# age = age.split(',')

# ------------------------------------------------------
''' kak zakrit' funkciju ????????????????????????'''
# import lib
# lib.drawbox()

# from lib import drawbox
# drawbox()

# def drawbox(width = int(input('Enter a width --->')), height = int(input('Enter a heigth ---> ')), outline = input('Enter a symbol for outline ---> '), fill = input('Enter a last symbol ---> ')):
# 	if (width < 2) or (height < 2):
# 		print ('ERROR ---> Too small value for idth or height ------')
# 	print(outline * width)
# 	for _ in range(height - 2):
# 		print(outline + fill * (width - 2) + outline)
# 	print(outline * width)
# drawbox()

# ------------------------------------------------------
'''Pifagor teorema ---------------------BOOOK ---> 85'''
# def pifagor_triang(a = float(input('Enter the first side lenght --->')), b = float(input('Enter the second side lenght --->'))):
#     from math import sqrt
#     c = sqrt(a ** 2 + b ** 2)
#     return round(c, 4)
# print(pifagor_triang())

'''Taxi price -------------------------BOOOK ---> 86'''
# def taxiprice(a = int(input('Enter a raod lenght in km ---> '))):
#     summ = 4.0
#     m1 = 0.25
#     for _ in range(140, a * 1000 + 140, 140):
#         summ += m1
#     return summ
# print(taxiprice())

'''Delivery price -------------------------BOOOK ---> 87'''
# def item(a = int(input('Enter the amount of bought items ---> '))) -> float:
#     x = 10.95
#     y = 2.95
#     if a == 1:
#         return f'{x}$'
#     elif a == 0:
#         return 'U do not put item in stash :('
#     for _ in range(2, a + 1):
#         x += y
#     return f'{round(x, 2)} $' 
# print(item())

'''The median of the numbers -------------------------BOOOK ---> 88'''
# def mediannumber(*a:int):
#     mylist = []
#     while a != 0:
#         a = int(input('Enter a number ---> '))
#         mylist.append(a)
#     mylist.pop()
#     mylist.sort()
#     if len(mylist) % 2 == 0:
#         x = len(mylist) / 2
#         for i in range(len(mylist) + 1):
#             if i == x:
#                 y = (mylist[i] + mylist[i - 1]) / 2
#                 return round(y, 4)
#     else:
#         x = len(mylist) / 2
#         for i in range(len(mylist) + 1):
#             if i == int(x):
#                 return mylist[i]
# print(mediannumber())

'''The numbers to ... -------------------------BOOOK ---> 90'''
def ordinalDate( d, m, y ):
    y_is_leap  = y % 400 == 0 or y % 4 == 0 and y % 100 != 0
    month_days = [31,28+y_is_leap,31, 30,31,30, 31,31,30, 31,30,31]
    md = 0
    for i in range(m-1):
        md += month_days[i]
    return md + d
d, m, y = list( map( int, input( 'день, месяц, год: ' ).split(',') ) )
print( f'Порядковый номер дня в году: { ordinalDate(d,m,y) }\n' )






