from turtle import heading
from numpy import square


class Rectangle:
    def __init__(self,width,height) -> None:
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return (self.width**2+self.height**2)**0.5
    def get_picture(self):
        if self.width>50 or self.height>50:
            return  "Too big for picture."
        pic=''
        for i in range(self.height):
            pic+=self.width*'*'
            pic+='\n'
        return pic
    def get_amount_inside(self,shape):
        answer=round(self.get_area()/shape.get_area())
        if answer==2:
          return 1
        return answer
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self,side) -> None:
        self.side=side
        self.width=side
        self.height=side
    def set_side(self,side):
        self.side=side
        self.width=side
        self.height=side
    def set_height(self, height):
        self.side=height
    def set_width(self, width):
        self.side=width
    def __str__(self) -> str:
        return f"Square(side={self.side})"

my_square=Square(4)
print(my_square)
print(my_square.get_picture())
my_square.set_side(3)
print(my_square.get_picture())

