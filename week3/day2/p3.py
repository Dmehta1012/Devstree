def op(fun,x,y):
    return fun(x,y)
def add(a,b):
    return a+b
def mul(a,b):
    return a*b

result_add=op(add,5,3)
print("Addition is->",result_add)
result_mul=op(mul,5,3)
print("Multiplicationis->",result_mul)
