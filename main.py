# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Product:
    name = "My Product"
    price = 3.99

class TotalCost:
    number_of_items = 10
    item_cost = 5.50

# note self is a keyword that the class is asking for inside the method parameter
    def print_values():
        print(TotalCost.number_of_items * TotalCost.item_cost)

TotalCost.print_values()