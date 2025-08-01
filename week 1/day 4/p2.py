print("Welcome to the calculator ")

num1=int(input("Enter any  num1: "))
num2=int(input("Enter any  num2: "))


print("\______________________________________/")
print("select your choice ")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for divsion")
num=int(input("Enter any from 1 to 4 number: "))

if num==1:
    print("your ans:",num1+num2)
elif num==2:
    print("your ans:",num1-num2)
elif num==3:
    print("your ans:",num1*num2)
elif num==4:
    if num1!=0 and num2!=0:
        print("your ans:",num1/num2)
    else:
        print("Can't divisible by zero")
else:
    print("enter valid choice")