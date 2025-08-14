# try:
#     a=int(input("Enter any number"))
#     sum=10/a
#     print("Sum:",sum)

# except ValueError:
#     print("Enter valid number")
# except ZeroDivisionError:
#     print("Number can not Divide with zero")


# try:
#     a=int(input("Enter any number"))

# except ValueError:
#     print("invalid error")

# else:
#     print(f"You enter {a}")
class InvalidIndexError(Exception):
    pass
try:
    try:
        empty_list = []
        enter_item = int(input("How many items to enter in list: "))
        for i in range(enter_item):
            l = input("Enter anything to put in list: ")
            empty_list.append(l)
        print("Your list:", empty_list)
    except ValueError:
        print(" Invalid input for number of items!")

    a = int(input("Enter any index number to check: "))

    if a<0 or a>len(empty_list):
        raise InvalidIndexError(f"Index {a} is out of range")
    
    print(f"Item at index {a}: {empty_list[a]}")

except InvalidIndexError as e:
    print(f"Custom Error:{e}")
except ValueError:
    print(" Please enter a valid integer for index!")
