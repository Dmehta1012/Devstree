n = int(input("Enter number of rows for the pyramid: "))
print("incresing  triangle ")
for i in range(n):
    for j in range(i+1):
        print(" *",end='')
    print()
print("Decreasing triangle")   
for i in range(n):
    for j in range(i,n):
        print(" *",end='')
    print()

print("Right side triangle")
for i in range (n):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()
print("left sid trinagle")
for i in range(n):
    for j in range (i+1):
        print(" *",end='')
    print("")
print("hills paterns")
for i in range(n):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i+1):
        print("*",end='')
    print("")
print("down hills patterns")
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n-1):
        print("*",end='')
    for j in range(i,n):
        print("*",end='')
    print("")

print("diamond patterns")
for i in range(n-1):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i+1):
        print("*",end='')
    print("")
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n-1):
        print("*",end='')
    for j in range(i,n):
        print("*",end='')
    print("")