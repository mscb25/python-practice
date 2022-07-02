#creation of a rectangle class

class Rectangle:
    
    #initializing the coordinates of the rectangle
    def __init__(self, x1, x2, y1, y2):
        if x1 < x2 and y1 > y2:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
        else:
            print("Not proper coordinates")
    def __str__(self):
        return(str(self.x1)+', '+str(self.y1)+', '+str(self.x2)+', '+str(self.y2))

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y1 - self.y2

    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return self.width() * 2 + self.height() * 2
    

class Square(Rectangle):
    def __init__(self, x1, y1, length):
        x2 = x1 + length
        y2 = y1 + length
        super().__init__(x1, y1, x2, y2)


r = Rectangle(9, 12, 14, 11)
