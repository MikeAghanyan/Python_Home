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