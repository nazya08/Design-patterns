class Shape:
    def accept(self, visitor):
        pass


class Circle(Shape):
    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def accept(self, visitor):
        visitor.visit_rectangle(self)


class Triangle(Shape):
    def accept(self, visitor):
        visitor.visit_triangle(self)


class ShapeVisitor:
    def visit_circle(self, circle):
        print("Calculating area and perimeter of the circle.")

    def visit_rectangle(self, rectangle):
        print("Calculating area and perimeter of the rectangle.")

    def visit_triangle(self, triangle):
        print("Calculating area and perimeter of the triangle.")


# Usage
shapes = [Circle(), Rectangle(), Triangle()]
visitor = ShapeVisitor()

for shape in shapes:
    shape.accept(visitor)
