def tri(x, y, z):
    a = x + y + z
    return a

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
        return 'ERROR'
        # rise ValueError

'''To find max of two numbers'''



    
