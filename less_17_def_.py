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
# def summ(*x):


def summ(*x):
    a = 0
    while x != 0:
        x = int(input('Enter a number ---> '))
        a += x
    return a
print(summ())

# ------------------------------------------------------
'''BOOOK ---> '''
# def item(a) -> float:
#     x = 10.95
#     if a == 1:
#         return x
#     elif a >= 2:
#         x += a * 2.95
#         return x
#     else:
#         return 'ERROR'

# print(item(3))





