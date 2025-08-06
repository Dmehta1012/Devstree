import math
def main():
    while True:
        print(" select any from following ")
        print("1.Area Calculator")
        print("2.Temperature Calculator")
        print("3.Quit")
        choice=input("Enter between (1-3)")
        match choice:
            case "1":
                def area_calculator():
                    print("choose shape  to calculate area\n")
                    print("1.Rectangle")#a=l*b
                    print("2.Square")#a=s*2
                    print("3.Circle")#area = math.pi * radius ** 2
                    print("4.Triangle")# area = 0.5 * base * height

                    choice=input("Enter the number to calculate the shape area ")

                    if choice=="1":
                        length=float(input("Enter length of Rectangle"))
                        breadth=float(input("Enter Breadth of Rectangle"))
                        area=length*breadth
                        print("area of Rectangle is:- ",area)

                    elif choice =="2":
                        side=float(input("Enter the side of Square"))
                        area=side**2
                        print("Area of Square is:-",area)

                    elif choice=="3":
                        radius=float(input("Enter radius of Circle"))
                        area=math.pi*radius**2
                        print("Area of Circle is:-",area)

                    elif choice=="4":
                        base=float(input("Enter the base of Triangle"))
                        height=float(input("Enter height of Triangle "))
                        area=0.5*base*height
                        print("Area of Triangle is:-",area)
                    else:
                        print("Invalid choice! Please enter number from 1-4")
                area_calculator()
            
            case "2":
                def temp_calculator():
                    while True:
                        print("Welcome to Temperature Calculator")
                        print("1.Celsius <--> Fahrenheit")
                        print("2.Celsius <--> Kelvin")
                        print("3.Fahrenheit <--> Kelvin")
                        print("4.Exit")

                        choice=input("Enter 1-4 to calculate->")

                        match choice:
                            case "1":
                                print("1.Celsius to Fahrenheit:")
                                print("2.Fahrenheit to Celsius:")

                                c=input("Enter 1-2 to select->")
                                if c=="1":
                                    print("Calculate Celsius to Fahrenheit")
                                    celsius=float(input("Enter Celsius-> "))
                                    Fahrenheit=(celsius*9/5)+32
                                    print("Celsius to Fahrenheit->",Fahrenheit)
                                elif c=="2":
                                    print("Calculate Fahrenheit to Celsius")
                                    fahrenheit=float(input("enter Fahrenheit->"))
                                    Celsius=(fahrenheit-32)*5/9
                                    print("Fahrenheit to Celsius->",Celsius)

                                else:
                                    print("Invalid Number! please Enter form 1-2 \n")
                            case "2":
                                print("1.Celsius to Kelvin")
                                print("2.Kelvin to Celsius")
                                print("3.Quit\n")
                                c=input("Enter 1-2 to select")
                                if c=="1":
                                    print("Calculate Celsius to Kelvin")
                                    celsius=float(input("Enter Celsius-> "))
                                    Kelvin=celsius+273.15
                                    print("Celsius to Kelvin->",Kelvin)
                                elif c=="2":
                                    print("Calculate Kelvin to Celsius")
                                    Kelvin=float(input("Enter Kelvin->"))
                                    celsius=Kelvin-273.15
                                    print("Kelvin to Celsius->",celsius)

                                else:
                                    print("Invalid Number! please Enter form 1-2 \n")
                            case "3":
                                print("Calculate Fahrenheit <--> Kelvin")
                                print("1.Fahrenheit to Kelvin")
                                print("2.Kelvin to Fahrenheit")
                                print("3.Quit\n")
                                c=input("Enter 1-2 to select")
                                if c=="1":
                                    print("Calculate Fahrenheit to Kelvin")
                                    Fahrenheit=float(input("Enter Fahrenheit-> "))
                                    Kelvin=(Fahrenheit-32)*5/9+273.15
                                    print("Celsius to Kelvin->",Kelvin)
                                elif c=="2":
                                    print("Calculate Kelvin to Fahrenheit")
                                    Kelvin=float(input("Enter Kelvin->"))
                                    Fahrenheit=(Kelvin-273.15)*9/5+32
                                    print("Kelvin to Celsius->",Fahrenheit)
                                else:
                                    print("Invalid Number! please Enter form 1-2 \n")
                            case "4":
                                    print("Thanks")
                                    break
                            case _:
                                print("Invalid choice! Please enter a number between 1 and 4.\n")
                temp_calculator()
            case "3":
                print("Good Bye!")
                break
main()