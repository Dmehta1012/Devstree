n=input("Hey! what is your name")
print(f"hello {n}")

grade=int(input("Enter your grade"))
print(f"your grade is {grade}")

if grade>=90:
    print(f"Grade {grade}=A")
elif grade>=65:
    print(f"Grade {grade}=B")
elif grade>=55:
    print(f"Grade {grade}=C")
elif grade>=45:
    print(f"Grade {grade}=D")
elif grade>=35:
    print(f"Grade {grade}=E")
elif grade<=35:
    print("FAIL")
else:
    print("Invalid writen type")