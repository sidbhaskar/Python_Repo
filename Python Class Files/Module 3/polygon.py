class polygon:
    def render(self):
        print('Rendering Polygon')

class square(polygon):
    def render(self):
        print("Rendering Square")

class circle(polygon):
    def render(self):
        print("Rendering Circle")

s1 = square()
s1.render()

c1= circle()
c1.render()

