# mylist = [1, 2, 3]
# print(mylist.count)

# class Test:
#     def func(self):
#         return 'OK'

# x = Test()
# print(x.func)

# import time
# from typing import Callable, Any
# import functools

# def timer(func:Callable) -> Any:
#     @functools.wraps(wrapped=func)
#     def timer_counter(*args):
#         '''TIMER COUNTER'''
#         st = time.time()
#         func(*args)
#         et = time.time()
#         return et - st
#     return timer_counter

# @timer
# def number_s() -> list[int]:
#     '''
#     Best func
#     '''
#     return [i ** 2 for i in range(10000)]

# @timer
# def number_c() -> list[int]:
#     return [i ** 3 for i in range(10000)]

# @timer
# def number_n(n:int) -> list[int]:
#     return [i ** n for i in range(10000)]

# print(number_s())
# print(number_c())
# print(number_n(3))

# print(number_s.__doc__)

# --------------------------------------------------------------------------------------

'''Decorators.basic #1 'Kak Dela?' '''

# from typing import Callable, Any
# import functools

# def how_are_you(test:Callable) -> Any:
#     @functools.wraps(wrapped=test)
#     def ask_question(*args):
#         '''Question about mood'''
#         question = (input('How are u? ')) 
#         ''' Sad answer '''       
#         print('By the way, I am not okay ;c \n--->Here is ur function') 
#         '''
#         Calling the function
#         '''
#         return test(*args)
#     return  ask_question


# @how_are_you
# def test():
#     print('<Тут что-то происходит...>')
# test()

'''Decorators.basic #2 'Slow down runing code' '''

# from typing import Callable, Any
# import functools
# import time

# def slow_down(test:Callable) -> Any:
#     @functools.wraps(wrapped=test)
#     def few_seconds_slow_down(*args):
#         '''slowing down'''
#         time.sleep(3)
#         return test()
#     return few_seconds_slow_down



# @slow_down
# def test():
#     print('<Тут что-то происходит...>')
# test()

'''Decorators.basic #3 'Logging' '''

# from typing import Callable, Any
# import functools
# import datetime

# def logging(func:Callable) -> Any:
#     @functools.wraps(wrapped=func)
#     def update_file(*args, **kwargs):
#         ''' If ur func has ERRORs, creat new file or update created with ERROR and continue '''
#         try:
#             print(func(*args, **kwargs))
#         except Exception as exception:
#             with open('Error_func.txt', 'a') as file:
#                 file.write(f'In {func.__name__} ----- {exception.__class__.__name__} ----- {datetime.datetime.now()}\n' )
#     return update_file

# @logging
# def calculator(a:float, c:str('symbol'), b:float) -> float:
#     '''This is calculator'''
#     if c == '+':
#         return float(a) + float(b)
#     elif c == '-':
#         return float(a) - float(b)
#     elif c == '/':
#         return float(a) / float(b)
#     elif c == '*':
#         return float(a) * float(b)
    
# calculator(input('Enter number1: '), input('Enter char: '), input('Enter number2: '))

''' -------------------------- WROOOOOOOONGGGGGGGGGGGGGGGGGGGG !!!!!!!!!!!!!! -------------------------- '''
# from typing import Callable, Any
# import functools

# def logging(test:Callable) -> Any:
#     @functools.wraps(wrapped=test)
#     def update_file(*args):
#         ''' If file has error update file with it's error and continue '''
#         try:
#             print()
#             # with open('func_error.txt', 'a') as file:
#             #     return file.write('1')
#         except BaseException:
#         # except (KeyError, TypeError, AttributeError, SyntaxError):            
#             with open('func_error.txt', 'a') as file:
#                 file.write('1')
#     return update_file
'''-------------------------- WRONG ANSWER ABOVE --------------------------'''






'''Decorators.basic #4 'Count' '''
# from typing import Callable, Any

# class Counter:

#     dec_count = 0
#     func_count = 0

#     def __init__(self, func_count) -> None:
#         Counter.dec_count += 1
#         self.func_count = func_count

#     def __call__(self, **kwargs) -> None:
#         self.func_count += 1
#         return kwargs.__name__

class Counter:

    count = 0

    def __init__(self, *args):
        Counter.count += 1

    def __call__(self):
        return f'{self.count}'



@Counter
def test():
    return 'Hello'

@Counter
def func():
    return 'Hello'

@Counter
def show():
    return 'Hello'    

@Counter
def show_print():
    return 'Hello'

print(func())