def plus(x):
    a = ['+',x]
    return a

def minus(x):
    a = ['-',x]
    return a

def times(x):
    a = ['*',x]
    return a

def div(x):
    a = ['/',x]
    if x==0:
        raise ValueError('Division by zero.')
    return a

def zero(a = None):
    this_num=0
    if a: # function is called first if a!=None
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: # function is called second
        return 0

def one(a = None):
    this_num=1
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 1

def two(a = None):
    this_num=2
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 2

def three(a = None):
    this_num=3
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 3

def four(a = None):
    this_num=4
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 4

def five(a = None):  
    this_num=5
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return 5

def six(a = None): 
    this_num=6
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 6

    
def seven(a = None):
    this_num=7
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 7

def eight(a = None):  
    this_num=8
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 8

def nine(a = None):  
    this_num=9
    if a: 
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: 
        return 9


