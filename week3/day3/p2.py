class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grade=[]

    def add_grade(self,grade):
        self.grade.append(grade)

    def average_grade(self):
        if not self.grade:
            return 0.0
        return sum(self.grade)/len(self.grade)
    
    def display(self):
        avg=self.average_grade()
        print(f"Name:{self.name},Age:{self.age},Grade:{self.grade},Average:{avg:.2f}")

Devarsh=student("Devarsh",20)
Rakesh=student("Rakesh",50)

Devarsh.add_grade(90)
Devarsh.add_grade(60)
Devarsh.add_grade(70)
Rakesh.add_grade(50)
Rakesh.add_grade(40)
Rakesh.add_grade(90)

Devarsh.display()
Rakesh.display()