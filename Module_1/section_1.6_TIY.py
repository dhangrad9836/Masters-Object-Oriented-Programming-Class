#order class
class Order:
    def __init__(self, n, l):
        self.order_number = n
        self.list_of_products = l

    #destructor method
    def __del__(self):
        print("order object destroyed")



#circle class
class Circle:
    def __init__(self, r, c):
        self.radius = r
        self.colour = c


    def __del__(self):
        print("circle object destroyed")

#objects
my_order = Order(554, ["apple", "banana"])
del my_order
# print(id(order3))  ......this will not run b/c the above del destructor deleted the object from memory

