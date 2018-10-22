class Shape(object):
    @property
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__()
        self.width=width
        self.height=height

    @property
    def area(self):
        return self.width*self.height

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

class Ellipase(Shape):
    pi=3.14
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b

    @property
    def area(self):
        return self.a*self.b*self.pi

class Circle(Ellipase):
    def __init__(self,r):
        super().__init__(r,r)


shapes=[Ellipase(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipase(10,20)]

areas=[x.area for x in shapes]
print('areas:', areas)
total_area=sum(areas)
print('total_area:', total_area)
















    
    
