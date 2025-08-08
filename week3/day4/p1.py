class Animal:
    def speak(self):
        self.Dog=Dog
        self.cat=cat
        print("ANIMAL CAN SPEAK")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

class cat(Animal):
    def meow(self):
        print("Cat meow")

c=cat()
c.speak()   
c.meow()
d=Dog()
d.speak()
d.bark()
