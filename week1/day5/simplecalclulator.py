while True:
    print("Welcome to calculator")
    print("1.Addition")
    print("2.Multiplication")
    print("3.Subtraction")
    print("4.Division")
    print("5.Quit\n")

    choice=int(input("Enter your choice between(1-5)"))
    
    match choice:
        case 1:
            n1=float(input("Enter n1->"))
            n2=float(input("Enter n2->"))
            sum=n1+n2
            print("Addition->\n",sum)
        
        case 2:
            n1=float(input("Enter n1->"))
            n2=float(input("Enter n2->"))
            mul=n1*n2
            print("Multiplication->\n",mul)
        
        case 3:
            n1=float(input("Enter n1->"))
            n2=float(input("Enter n2->"))
            sub=n1-n2
            print("Subtraction->\n",sub)
        case 4:
            n1=float(input("Enter n1->"))
            n2=float(input("Enter n2->"))
            if n1!=0 or n2!=0:
                div=n1/n2
                print("Division->\n",div)
            else:
                print("number can not divide with zero ")
        case 5:
            print("Good Bye!")
            break

