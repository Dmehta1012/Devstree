def fun(*args):
    return sum(args)
print(fun(10,20,10))
print(fun(100,500,100))

def key(**kwargs):
    for k ,val in kwargs.items():
        print(k,val)
key(Name="= Devarsh",city="= Ahmedabad")