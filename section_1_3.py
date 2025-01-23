# Create the default and parameterized constructors for the following

class Order:
    order_number = 0
    list_of_products = []


    #parameterized constructor
    def __init__(self, order_num, product_list):
        self.order_number = order_num
        self.list_of_products = product_list

    def print_order(self):
        print(self.order_number)

    def print_list_of_products(self):
        print(self.list_of_products)

############################################### Circle class

class Circle:
    radius = 0
    colour = "none"

    # default constructor
    #self is the default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, radius, color):
        self.radius = radius
        self.colour = color

    #method
    def print_circle(self):
        print(self.colour)

    def print_radius(self):
        print(self.radius)


#call the order
order1 = Order(123, ["apple", "orange"])
order1.print_order()
order1.print_list_of_products()


#call the circle
circle1 = Circle(4, "greeen")
circle1.print_circle()
circle1.print_radius()
# circle1.radius = 4
# circle1.colour = "Green"