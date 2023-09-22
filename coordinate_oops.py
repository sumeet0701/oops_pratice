
"""
Write OOPS Classes to handle the following senarios:
1. A user can create and view 2d Coordinates
2. A user can find out the distance between 2 coordinates
3. A user can find out the distance of a coordinate from origin
4. A user can check if point lies on line or not
5. A  user can find out the distance between 2 coordinates and line
"""

class Coordinates:
    def __init__(self, x ,y) :
        self.x_cord = x
        self.y_cord = y
    
    def __str__(self):
        return "<{},{}>". format(self.x_cord, self.y_cord)
    
    def distance_euc(self, other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5
     
    def distance_origin(self):
        return self.distance_euc(Coordinates(0,0))
        # Alternative solution
        # return (self.x_cord**2 - self.y_cord**2)**0.5


class line:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "{}x + {}y+ {} = 0".format(self.a, self.b, self.c)
    
    def point_on_line(line, coordinates):
        if line.a * coordinates.x_cord + line.b *coordinates.y_cord + line.c == 0:
            return "point is on Line"
        else:
            return "point doesnot lie on Line"
    
    def distance_line_point(line, coordinates):
        return (abs(line.a* coordinates.x_cord + line.b*coordinates.y_cord + line.c)/(line.a**2 +line.b**2))**0.5
        

    
    
l1 = line(1,1,-2)
p1 = Coordinates(5,1)

print(l1.distance_line_point(p1))
