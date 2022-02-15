#creat circle class
#data attributes: radius <-private
#property called radius reterns current radius
#setter called radius allows you to set a radius greater than 0
#method get_area
class circle:
    def __init__(self, radius):
        self.__radius = radius #dunderscore makes it private

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            raise ValueError("new radius must be greater than 0")

    def get_area(self):
        area = 3.14*self.radius**2
        return area

my_circle = circle(5)
print(my_circle.get_area())
