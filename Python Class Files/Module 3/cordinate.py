class Circle(object):
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

    def draw(self,canvas):
        rad = self.radius
        x1 = self.center[0] - rad
        x2 = self.center[0] - rad
        y1 = self.center[1] - rad
        y2 = self.center[1] - rad

#decleare a class called elecrticity with 2 attributes cusumer id ,current reading, previous reading , number of units used,create values of number of units used

#create a class supermarket define any 3 attributes , and display their bills , with date , titles , price