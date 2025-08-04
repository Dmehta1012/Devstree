grade=[]

for subject in ["Maths","Science","English","Hindi"]:
    marks=float(input(f"Enter {subject}  marks (0-100)"))
    if 0 < marks < 100:
        grade.append(marks)
        # print(f"your {subject} Marks (0-100)")
    else:
        print("Invalid marks ")
total=sum(grade)
average=sum(grade)/len(grade)
heighest=max(grade)
lowest=min(grade)
print(f"total{total}:")
print(f"average:{average}")
print(f"heighest:{heighest}")
print(f"lowest:{lowest}")

if average >= 90:
    print("Grade A")
elif average >= 70:
    print("Grade B")
elif average >= 50:
    print("Grade C")
elif average >= 40:
    print("Grade D")
else:
    print("Fail")
