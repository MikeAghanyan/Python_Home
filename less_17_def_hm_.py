import time

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

'''Password Generator -----------BOOK_100'''

# def passwordGenerator(a:int, n:int):
#     import random
#     lenght = random.randint(a, n)
#     pas = ''
#     for i in range(lenght):
#         pas += chr(random.randint(33, 126))
#     return pas

# print(passwordGenerator(115, 115))

'''Car number -----------BOOK_101'''
# import time

# def carnumber():

    # import random
#     alpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     num = '123456789'
#     a_list = []
#     n_list = []
#     a_count = 0
#     n_count = 0
#     c_num = ''

#     for i in alpha:
#         a_list.append(i)

#     for i in num:
#         n_list.append(i)

#     newcarnum = random.randint(0, 1)

#     if newcarnum == 1:
#         n = 4
#         while n_count != n:
#             c_num += random.choice(n_list)
#             # random.shuffle(n_list)
#             # c_num += n_list[1]
#             n_count += 1
#         while a_count != 3:
#             c_num += random.choice(a_list)
#             a_count += 1
#         return f'Ur car number is ---> {c_num}'

#     else:
#         n = 3
#         while a_count != 3:
#             c_num += random.choice(a_list)
#             a_count += 1
#         while n_count != n:
#             c_num += random.choice(n_list)
#             # random.shuffle(n_list)
#             # c_num += n_list[1]
#             n_count += 1
#         return f'Ur car number is ---> {c_num}'

# st = time.time()
# print(carnumber()) 
# et = time.time()
# print(et - st)

'''Password check -----------BOOK_102'''

# def passwordCheck(pas:str): #'Enter ur password'
#     symb = '!@#$%^&*()_+<>?:"|[{]}/;~`-=\,./'
#     num = '1234567890'
#     upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     if len(pas) < 8 or (' ' in pas):
#         return ValueError('--------------- Not enought symbols --------------- \n********* Minimum 8 symbols and no spaces *********')              
#     else:
#         if upper in pas < 2:
#             return ValueError('------------- Minimum 2 upper letter ------------- '  )
#         else:
#             if (symb in pas < 2) and (num in pas < 2):
#                 return ValueError('------------- Minimum 2 symbols and 2 numbers ------------- '  )  
#             else:
#                 return '----- !!!!---------- Congrats ----- it is a strong password ----- !!!!---------- '
# st = time.time()
# print(passwordCheck('ajtha;vkh;dgh;anvh;avihga;sdkghi4765489y543tW VEG ADSFBJK'))
# et = time.time()
# print(et - st)

'''PasswordGeneratorV03 -----------BOOK_102'''

# def passwordGeneratorV03(keyword:str) -> str:
#     import random
#     num = '123456789'
#     symb = '!@#$%^&*()_+<>?:"|[{]}/;~`-=\,./'
#     upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     for _ in range (4, 8):
#         keyword += random.choice(keyword)
#         keyword += random.choice(num)
#         keyword += random.choice(symb)
#         keyword += random.choice(upper)
#     return keyword
# print(passwordGeneratorV03('.'))

'''String in the middle -----------BOOK_93'''


