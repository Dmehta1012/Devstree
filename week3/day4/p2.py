import math
class shape:
    def calculate_area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def calculate_area(self):
        return math.pi*self.radius*2
    
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.width*self.length

class triangle(shape):
    def __init__(self,base,heigth):
        self.base=base
        self.heigth=heigth
    
    def calculate_area(self):
        return 0.5*self.base*self.heigth
    
circle=circle(7)
rectangle=rectangle(10,5)
triangle=triangle(6,4)

print(f"Calculate are of circle {circle.calculate_area()}")
print(f"Calculate are of Rectangle {rectangle.calculate_area()}")
print(f"Calculate are of Triangle {triangle.calculate_area()}")
        
                

        