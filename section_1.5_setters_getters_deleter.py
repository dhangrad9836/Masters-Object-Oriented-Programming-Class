# Create the default and parameterized constructors for the following

class Order:
    _order_number = 0
    list_of_products = []


    #parameterized constructor
    def __init__(self, order_num, product_list):
        self._order_number = order_num
        self.list_of_products = product_list

    #getter method
    @property
    def order_number(self):
        print("getter method used")
        return self._order_number

    #setter method
    @order_number.setter
    def order_number(self, order_number):
        print("setter method useed")
        self._order_number = order_number

    @order_number.deleter
    def order_number(self):
        print("deleter method used")
        del self._order_number

    def print_list_of_products(self):
        print(self.list_of_products)



############################################### Circle class

class Circle:
    _radius = 0
    _colour = "none"

    # default constructor
    #self is the default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, radius, color):
        self._radius = radius
        self._colour = color

    #getter method
    @property
    def colour(self):
        print("color getter method")
        return self._colour

    @property
    def radius(self):
        print("radius getter method")
        return self._radius

    #setter method
    @colour.setter
    def colour(self, colour):
        print("colour setter method")
        self._colour = colour

    @radius.setter
    def radius(self, radius):
        print("radius setter method")
        self._radius = radius

    #deleter method
    @colour.deleter
    def colour(self):
        print("Colour deleter method")
        del self._colour

    @radius.deleter
    def radius(self):
        print("Radius deleter method")
        del self._radius

    #method
    # def print_circle(self):
    #     print(self.colour)
    #
    # def print_radius(self):
    #     print(self.radius)


#call the order
order1 = Order(123, ["apple", "orange"])
order1.order_number = 545
getOrderNum = order1.order_number
del order1.order_number
#order1.print_list_of_products()


#call the circle
circle1 = Circle(4, "greeen")
circle1.colour = "orange"
circle1.radius = 5
c1 = circle1.colour
c2 = circle1.radius

del circle1.colour
del circle1.radius


# num1 = 45
# num2 = num1
# print(id(num1))
# print(id(num2))