#functions for meal program

#this function calculates the main cost by increasing the value of total by the value of the main dishes entry with
#the key that the user entered.....in for loop: k is for the key and v is for the value for the dictionary
#this takes in the user input and the main dictionary of key/values
def calc_main_cost(m_type, m_dict):
    #declare variable total as global to modify it in the function
    global total
    for k, v in m_dict.items():
        #if the key ie: meal name is equal to the users input of the meal they entered then add the value or price
        #to the total
        if k == m_type:
            total += v

def get_side_order():
    side_order = input("Choose a side order by typing its name OR enter Q to quit: ")
    return side_order

#this function calculates the side order cost by increasing the value of total by the value of the side order entry with
#the key that the user entered.....in for loop: k is for the key and v is for the value for the dictionary
def add_side_order(s_type, s_dict):
    # declare variable total as global to modify it in the function
    global total
    for k, v in s_dict.items():
        if k == s_type:
            total += v


###############################################################################################


# dictionary of main dishes and their prices
main = {"Burger": 10.55, "Club Sandwich": 8.45, "Rump Steak" : 15.40, "Ceasar Salad": 9.95, "Fish and Chips": 10.95}

# dictionary of side dishes and their prices
side = {"Loaded Chips": 3.65, "Seasonal Salad": 3.15, "Onion Rings": 3.45, "Garlic Bread": 2.50, "Cheese Platter": 4.95}

# ask for user input with main_type is for the main dish
main_type = input("Choose a main by typing its name OR enter Q to quit: ")
total = 0.0

#main loop of the program
while main_type != "Q":
    if main_type in main.keys():
        #check user input and put entire dictionary main inside calc_main_cost function
        #so if user input is valid from above if statement then put user input and main dictionary inside
        # the calc_main_cost function
        calc_main_cost(main_type, main)
        side_order = get_side_order()
        while side_order != "Q":
            if side_order in side.keys():
                add_side_order(side_order, side)
            else:
                print("invalid input")
            side_order = get_side_order()
    else:
        print("invalid input")
    main_type = input("Choose a main by typing its name OR enter Q to quit: ")

print("Total cost of your order: {:.2f}".format(total))




























