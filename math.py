# add implmentation
def add(a, b):
    return a+b

# sub implmentation
def sub(a, b):
    return a-b    #changes commited on master branch

# mul implmentation
def mul(a, b):
    return a*b     #changes done at bug456

# div implmentation
def div(a, b):
    if b==0:         #changes done at bug789
        return "Divide by 0 error"
    else:
        return a/b
