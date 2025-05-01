class MealOrder:
    #class variables of main and side
    # dictionary of main dishes and their prices
    main = {"Burger": 10.55, "Club Sandwich": 8.45, "Rump Steak" : 15.40, "Ceasar Salad": 9.95, "Fish and Chips": 10.95}
    # dictionary of side dishes and their prices
    side = {"Loaded Chips": 3.65, "Seasonal Salad": 3.15, "Onion Rings": 3.45, "Garlic Bread": 2.50,
            "Cheese Platter": 4.95}

    #constructor
    # we have total and two empty lists to record the users choices of main and side dishes
    def __init__(self, total = 0.0):
        self.total = total
        self.ordered_main = []
        self.ordered_side = []

    #class methods
    def get_main_type(self):
        m_t = input("Choose a main by typing its name OR enter Q to quit: ")
        if m_t == "Q" or m_t in MealOrder.main.keys():
            return m_t
        else:
            return ""

    def get_side_type(self):
        s_t = input("Choose a side by typing its name OR enter Q to quit: ")
        if s_t == "Q" or s_t in MealOrder.side.keys():
            return s_t
        else:
            return ""


    def order(self):
        m_t = self.get_main_type()
        while m_t != "Q":
            if m_t != "":
                self.ordered_main.append(m_t)
                self.total += MealOrder.main[m_t]
                s_t = self.get_side_type()
                while s_t != "Q":
                    if s_t != "":
                        self.ordered_side.append(s_t)
                        self.total += MealOrder.side[s_t]
                    else:
                        print("invalid input")
                    s_t = self.get_side_type()
                else:
                    print("invalid input")
                m_t = self.get_main_type()


    #display cost
    def display_cost(self):
        print("Your order: ")
        for k, v in MealOrder.main.items():
            if k in self.ordered_main:
                print(k, ":", v)

        for k, v in MealOrder.side.items():
            if k in self.ordered_side:
                print(k, ":", v)
        print("The total cost of your order: {:.2f}.".format(self.total))

#object instantiation
meal = MealOrder()

meal.order()
meal.display_cost()