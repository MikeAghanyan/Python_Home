# class Myclass:

#     x = 10

# print(Myclass.x)

# class Change:

#     def __init__(self, usd) -> None:
#         self.usd = usd

#     def usd_to_amd(self):
#         return f'{self.usd * 390}(dram)'

# Mike = Change(int(input('Enter  USD ---> ')))
# print(Mike.usd_to_amd())

#  --------------------------------------------------------------------------------------------------

# class Soda:

#     def __init__(self, ingrd=None) -> None:
#         self.ingrd = ingrd

#     def show_my_drink(self):
#         if self.ingrd == None:
#             return 'Common Soda'
#         else:
#             if isinstance(self.ingrd, str):
#                 if self.ingrd.isalpha():
#                     return f'Soda with {self.ingrd}'
#             else:
#                 return '--- !!! --- Enter ingridients only --- !!! ---'
# Mike = Soda(input('Enter ingridient ---> '))
# print(Mike.show_my_drink())

#  --------------------------------------------------------------------------------------------------

# class TriangleChecker:

#     def __init__(self, a:float, b:float, c:float) -> None:
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_triangle(self):
#         if isinstance(self.a, str) or  isinstance(self.a, str) or  isinstance(self.a, str):
#             return 'Нужно вводить только числа!'
#         else:
#             if self.a <= 0 or self.b <= 0 or self.c <= 0: 
#                 return 'C отрицательными числами ничего не выйдет!'
#             else:
#                 if (self.a + self.b < self.c) or (self.b + self.c < self.a) or (self.a + self.c < self.b):
#                     return 'Жаль, но из этого треугольник не сделать!'
#                 else:
#                     return 'Ура, можно построить треугольник!'

# x = TriangleChecker('s', 'f', 8)
# print(x.is_triangle())

#  --------------------------------------------------------------------------------------------------

# class KgToPounds:

#     __kg = int(input('Enter kg ---> '))

#     def to_pounds(self, ):
#         return round((self.__kg * 2.204622), 3)

#     def set_kg(self, nor_kg):
#         self.__kg == nor_kg

#     def get_kg(self):
#         return self.__kg


# x = KgToPounds(5)
# print(x.get_kg())


# class Nikola:

#     __name = 'Николай'

#     def __init__(self,  name:str, years:int):
#         self.__name = name
#         self.__years = years

#     def set_name(self):
#         self.name = self.__name

#     def get_name(self):
#         if self.name == 'Николай':
#             return self.__name


# class RealString:

#     def __init__(self, word1, word2) -> bool:
#         self.word1 = word1
#         self.word2 = word2
    
#     def count(self):
#         return f'{self.word1} is bigger than {self.word2} ---> {len(self.word1) > len(self.word2)}'

# x = RealString('APLphabet', 'Великобритания')
# print(x.count())
            





    

#  --------------------------------------------------------------------------------------------------
# def accum(s):

#     a = ''

#     for j in range(len(s)):
#         for i in s:
#                 a += i * (j + 1)
#                 return a

# print(accum("ZpglnRxqenU"))

#  --------------------------------------------------------------------------------------------------

# def solution(number):

#     s = 0

#     for i in range(3, number):
#         if i % 5 == 0 or i % 3 == 0:
#             s += i 
#     return s       

# print(solution(1000))

# def alphabet_position(text):
    
#     # x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o','p','q','r','s', 't', 'u', 'v','w','x','y','z']
    
#     x = 'abcdefghijklmnopqrstuvwxyz'
#     abc = {}
#     output = ''
#     # # mylist = []
    
#     # for i in x:
#     #     mylist.append(i)

#     for j in x:
#         abc[j] = (x.index(j) + 1)

#     text = text.replace(' ', '')
#     text = text.lower()

#     for i in text:
#         if i.isalpha():
#             output += str(abc[i]) + ' '
#     output = output.rstrip()
#     return output

# print(alphabet_position("The sunset sets at twelve o'clock"))

# def add_length(str_):
#     mylist2 = []
#     mylist = str_.split(' ')
#     for i in mylist:
#         if len(i) < 0:
#             i = 0
#         else:
#             # i += ' ' + str(len(i))
#             mylist.pop(' ')
#             mylist.pop(len(i))
#     return mylist

# print(add_length('apple ban'))
# import math
# def find_even_index(arr):
#     a = [] 
#     if sum(a) == sum(arr):
#             return 0
#     for i in arr.copy():
#         arr.pop(arr.index(i))
        
#         if sum(a) == sum(arr):
#             m = a * b
#             while a != 0 and b != 0:
#                 if a > b:
#                     a %= b
#                 else:
#                     b %= a
#             return (m // (a + b))
#         a.append(i)
#     return -1

        
#     print()

# print(find_even_index([10,-80,10,10,15,35,20]))

# creat()


#  --------------------------------------------------------------------------------------------------
'''Lesson 25'''
# class First:

#     def __init__(self, first = None):
#         self.first = first

#     def name(self):
#         return self.first

# class Second(First):

#     def __init__(self, first, second = None):
#         super().__init__(first)
#         self.second = second

#     def my_dict(self):
    
#         my_dict = {}

#         for i, j in zip(self.second, self.first):
#             my_dict[i] = j
#         return my_dict
   
#         # for i in self.second:
#         #     for j in self.first:
#         #         my_dict[j] = i
#         #         self.second.remove(j)
#         #     self.first.remove(i)
#         # return my_dict

# first = ['Ani', 'Jessy ', 'Ben'] 
# second = [1,2,3]
# user = Second(first, second)

# print(user.my_dict())

# my_dict = {}
# for i in second.copy():
#     my_dict[i] = first[i-i]
#     second.pop(i-i)
#     first.pop(i-i)
# print(my_dict)   

#  --------------------------------------------------------------------------------------------------
'''ex - 3'''
class sum_of_multiplies():
    
    '''
    Class to solve the 3 exercise in lesson 27 presentation.
    '''
    def __init__(self, number:int = None, summ_all = None) -> None:
        self.num = number
        self.sum = summ_all

    def summ(self):

        import json

        '''
        function created to find the sum of all the multiples of 3 and 5 below the given number.
        '''
       
        self.num = int(input('Enter a number of searching range end ---> '))
        self.sum = 0
        for i in range(self.num):
            if (i % 3) == 0 or (i % 5 == 0):
                self.sum += i
        return self.sum
       
        # with open('3_5.json', 'w') as file:
        #     json.dump('Below {self.num} the summ of all the multiples of 3 and 5 is {self.sum}', file)

    # def to_json(self):
        
        

        
y = sum_of_multiplies()
print(y.summ())
# y.sum()


    






    


