'''MULTIPLY ??? kak umnozit' na 0.5??? i vvodit' float(*x)  ''' 

def multiply(*x:int) -> int:
    a = 1
    while x != '':
        x = input('Enter a number ---> ')
        if x == '':
            return a
        elif '.' in x:
            # isinstance(x, float, True)
            # if 
            a *= float(x)
            print(a)
        else: 
            a *= x
print(multiply())


''''''
    
# from typing import Callable, Any
# import functools

# def test_func(func:Callable) -> Any:
#     @functools.wraps(wrapped=func)
#     def test_decorator(*args):
#         return func(*args) ** 2
#     return test_decorator

# @test_func
# def func(a:int) -> int:
#     return a
# print(func(5))

# ------------------------------------------------------
# def print_hello():
#     '''Veradardznuma barev tim'''
#     return 'Hello Team'
# print(print_hello())
# print(print_hello.__name__)
# print(print_hello.__doc__)
# ------------------------------------------------------
# def func(a):
#     return a ** 2

# def main():
#     print(func(a))

# if __name__ == '__main__':
#     a = int(input('Enter number: '))
#     main()
# else:
#     print('Error')
# ------------------------------------------------------
# n = 10
# res = 1
# for i in range(1, n + 1):
#     res *= i
# print(res)

# def func(n):
#     if n == 0:
#         return 1
#     else:
#         return n * func(n - 1)
# print(func(10))

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
# print(fib(6))


# n = 18
# s = ''
# while n != 1:
#     s += str(n % 2)
#     n //= 2
# print(f'{n}{s[::-1]}')
# ----------------------------------
# def func(n, s = ''):
#     if n == 1:
#         return f'{n}{s[::-1]}'
#     else:
#         return func(n // 2, s + str(n % 2))
# print(func(18))
# ----------------------------------
