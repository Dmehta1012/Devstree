s=input(print("Enter a string:"))
print("original string "+s)

t=tuple(s)
print("after converting to tuple:",t)

l=list(s)
print("after converting to list:",l)

try:
    i=int(s)        
    print("after converting to int:",i)
except ValueError:
    print("Cannot convert string to int:", s)  