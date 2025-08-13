import csv

num_student = int(input("Enter number of student: "))

student = [["Name", "Math", "Science", "English", "Gujarati"]]

for i in range(num_student):
    print(f"\nEnter Student Details {i+1}:")
    name = input("Enter your name: ")
    math = input("Enter maths marks: ")
    science = input("Enter science marks: ")
    english = input("Enter english marks: ")
    gujarati = input("Enter gujarati marks: ")

    student.append([name, math, science, english, gujarati])


with open(r"C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day1\student.csv", "w", newline="") as f:
    write = csv.writer(f)
    write.writerows(student)


with open("student.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  

    with open(r"C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day1\res.txt", "w") as res:
        res.write("Student Results:\n")
        res.write("=================\n")
        for row in reader:
            name = row[0]
            marks = list(map(int, row[1:]))
            avg = sum(marks) / len(marks)
            print(f"{name}: {avg:.2f}")

            # Write each student result
            res.write(f"Name: {name}\n")
            res.write(f"Marks: {marks}\n")
            res.write(f"Average: {avg:.2f}\n")
            res.write("-----------------\n")

print("\n Results saved to res.txt")
