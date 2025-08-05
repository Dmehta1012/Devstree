n=input("Enter your name:")
print(f"hello {n}")

age=int(input("Enter your age "))
print(f"your age is {age}")

if age<=1:
    print("New born baby")
elif age<=13:
    print("you are child")
elif age<20:
    print("you are teeager")
elif age<=65:
    print("your are adult")
else:
    print("senior")