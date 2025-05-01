class Student:
    def __init__(self, name, number):
        self._name = name
        self.student_number = number

    def get_name(self):
        print("getter method used")
        return self._name

    def set_name(self, name):
        print("setter method used")
        self._name = name

    def del_name(self):
        print("Deleter method used")
        del self._name

    #property function used
    name = property(get_name, set_name, del_name)

student1 = Student("Rob", 1002030)
student1.name = "Robert"    #here we are accessing the setter method since we are setting a name
name1 = student1.name       #here we are accessing the getter method since we are just accessing the name variable
del student1.name