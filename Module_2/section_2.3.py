# MenuItem class
class MenuItem:
    def __init__(self, n, p):
        self.name = n
        self.price = p

# Menu class
class Menu:
    # list of main dishes and their prices
    main = [MenuItem("Burger", 10.44), MenuItem("Club Sandwich", 8.45),
            MenuItem("Rump Steak", 15.40), MenuItem("Caesar Salad", 9.95),
            MenuItem("Fish and Chips", 10.95)]

    # list of side dishes and their prices
    side = [MenuItem("Loaded Chips", 3.65), MenuItem("Seasonal Salad", 3.15),
            MenuItem("Onion Rings", 3.45), MenuItem("Garlic Bread", 2.50),
            MenuItem("Cheese Platter", 4.95)]

    # Methods of the Menu class
    #get the main dish
    def get_main_type(self):
        m_t = input("Choose a main type by typing its name OR enter Q to quit: ")
        for i in Menu.main:
            if(m_t == "Q" or m_t == i.name):
                return m_t
        return ""

    # get the side dish
    def get_side_type(self):
        s_t = input("Choose a side by typing its name OR enter Q to quit:")
        for i in Menu.side:
            if (s_t == "Q" or s_t == i.name):
                return s_t
        return ""


# Order class
class Order:
    def __init__(self, total = 0.0):
        self.total = total
        self.ordered_main = []
        self.ordered_side = []

        m_t = Menu.get_main_type()
        while m_t != "Q":
            if m_t != "":
                self.ordered_main.append(m_t)
                s_t = Menu.get_side_type(m_t)
                while s_t != "Q":
                    if s_t != "":
                        self.ordered_side.append(s_t)
                    else:
                        print("invalid input")
                        s_t = Menu.get_side_type()
            else:
                print("invalid input")
            m_t = Menu.get_main_type()


        # methods of Order class
        def display_cost(self):
            pass
      













