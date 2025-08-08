student = {}

s = int(input("Enter number of students: "))

for i in range(s):
    name = input(f"\nEnter name of student {i+1}: ")
    grades = []

    sub = int(input(f"How many grades for {name}? "))

    for j in range(sub):  # Use 'sub' here, not 's'
        g = int(input(f"Enter grade {j+1} for {name}: "))
        grades.append(g)

    student[name] = grades  # Save list of grades to student dictionary

# Print report
print("\nStudent Report:")
for name in student:
    grades = student[name]
    average = sum(grades) / len(grades)
    print(name, "Grades:", grades, "Average:", round(average, 2))

# Overall analysis
all_grades = []

for grades in student.values():
    for g in grades:
        all_grades.append(g)

overall_average = sum(all_grades) / len(all_grades)
highest_grade = max(all_grades)
lowest_grade = min(all_grades)

print("\nOverall Average:", round(overall_average, 2))
print("Highest Grade:", highest_grade)
print("Lowest Grade:", lowest_grade)


    