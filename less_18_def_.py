'''Parz tiv -----------BOOK_98'''
# def prime_num(n:int):

#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             return 'Parz chi'
#     else:
#         return 'Parz e'

'''next Parz tiv -----------BOOK_99'''
# def prime_num__(n:int):

#     while True:
#         n += 1
#         for i in range(2, n // 2 + 1):
#             if n % i == 0:
#                 break
#         else:
#             print(n)
#             break

'''Car number -----------BOOK_101'''
import random

alpha = 'qwertyuiopasdfghjklzxcvbnm'
num = '123456789'
a_list = []
n_list = []
a_count = 0
n_count = 0
c_alpha = ''
c_num = ''
for i in alpha:
    a_list.append(i)
while a_count != 3:
    random.shuffle(a_list)
    c_alpha += a_list[1]
    a_count += 1
for i in num:
    n_list.append(i)
    while n_count != 3:
        
print(c_alpha)   


    
# random.choices


# newcarnum = random.randint(0, 1)
# if newcarnum == 1:


# prime_num__(56)

# print(even_num(22))

