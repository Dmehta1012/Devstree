# # Square each number in the list
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x ** 2, numbers))
# print("Squares:", squares)
# # Output: Squares: [1, 4, 9, 16, 25]


# # Filter even numbers from the list
# numbers = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print("Even numbers:", evens)
# # Output: Even numbers: [2, 4, 6]

# # Sort list of tuples based on the second value
# students = [("Alice", 88), ("Bob", 72), ("Charlie", 95)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print("Sorted by marks:", sorted_students)
# # Output: Sorted by marks: [('Bob', 72), ('Alice', 88), ('Charlie', 95)]

add=lambda a,b:a+b
print(add(1,4))

mul=lambda a,b:a*b
print(mul(3,4))

n=[1,2,3,4,5,6,7,8,9,10]
square=list(map(lambda x:x**2,n))
print("Square",square)

n=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,n))
print("even Number",even)