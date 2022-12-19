'''summa storon Triugolnika'''
def tri(x, y, z):
    a = x + y + z
    return a

'''BOX'''
def drawbox(width = int(input('Enter a width --->')), height = int(input('Enter a heigth --->\
	')), outline = input('Enter a symbol for outline ---> '), fill = input('Enter a last symbol ---> ')):
	if (width < 2) or (height < 2):
		return ('ERROR ---> Too small value for idth or height ------')
	print(outline * width)
	for _ in range(height - 2):
		print(outline + fill * (width - 2) + outline)
	print(outline * width)

'''slide-CALCULATOR'''
def calculator(a:float, b:float, operator:str) -> float:
    if operator == '+':
        return a + b
    elif operator == '+':
        return a - b
    elif operator == '/':
        return a / b
    elif operator == '*':
        return a * b
    elif operator == '**':
        return a ** b
    elif operator == 'log':
        return __import__('math').log(a, b)
    else:
        # return 'ERROR'
        raise ValueError('Enter the numbers')

'''SUMMARY'''
def summ(*x) -> float:
    a = 0
    while x != 0:
        x = float(input('Enter a number ---> '))
        a += x
    return a

'''MULTIPLY'''
def summ(*x) -> float:
    a = 0
    while x != 0:
        x = float(input('Enter a number ---> '))
        a *= x
    return a

'''SUM ALL LETTERS AND NUMBERS'''
def allsumm(text = input('Enter the numbers and the letters ---> ')) -> str:
    a = 0
    b = '' # esli otdel'no to []
    for i in text:
        if i.isalpha():
            b += i
            # b.append(i)
        elif i.isdigit():
            a += int(i)
    return f'{b} is all used letters \n{a} is summmary of all used numbers'

'''The median of the numbers -------------------------BOOOK ---> 88'''
def mediannumber(*a:int):
    mylist = []
    while a != 0:
        a = int(input('Enter a number ---> '))
        mylist.append(a)
    mylist.pop()
    mylist.sort()
    if len(mylist) % 2 == 0:
        x = len(mylist) / 2
        for i in range(len(mylist) + 1):
            if i == x:
                y = (mylist[i] + mylist[i - 1]) / 2
                return round(y, 4)
    else:
        x = len(mylist) / 2
        for i in range(len(mylist) + 1):
            if i == int(x):
                return mylist[i]

'''Car number -----------BOOK_101'''
import random

def carnumber():
    alpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    num = '123456789'
    a_list = []
    n_list = []
    a_count = 0
    n_count = 0
    c_num = ''

    for i in alpha:
        a_list.append(i)

    for i in num:
        n_list.append(i)

    newcarnum = random.randint(0, 1)

    if newcarnum == 1:
        n = 4
        while n_count != n:
            random.shuffle(n_list)
            c_num += n_list[1]
            n_count += 1
        while a_count != 3:
            c_num += random.choice(a_list)
            a_count += 1
        return f'Ur car number is ---> {c_num}'

    else:
        n = 3
        while a_count != 3:
            c_num += random.choice(a_list)
            a_count += 1
        while n_count != n:
            random.shuffle(n_list)
            c_num += n_list[1]
            n_count += 1
        return f'Ur car number is ---> {c_num}'

'''Password Generator -----------BOOK_100'''

def passwordGenerator(a:int, n:int):
    import random
    lenght = random.randint(a, n)
    pas = ''
    for i in range(lenght):
        pas += chr(random.randint(33, 126))
    return pas
    
'''Password check -----------BOOK_102'''

def passwordCheck(pas:str): #'Enter ur password'
    symb = '!@#$%^&*()_+<>?:"|[{]}/;~`-=\,./'
    num = '1234567890'
    upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    if len(pas) <= 8:
        return ValueError('-------------Not enought symbols /Minimum 8 symbols/ ------------- '  )              
    else:
        if upper in pas < 2:
            return ValueError('------------- Minimum 2 upper letter  ------------- '  )
        else:
            if (symb in pas < 2)  and (num in pas < 2):
                return ValueError('------------- Minimum 2 symbols and 2 numbers ------------- '  )  
            else:
                return '----- !!!!---------- Congrats ----- it is a strong password ----- !!!!---------- '