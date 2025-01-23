class Student:
    def __init__(self, name, number):
        self._name = name
        self.student_number = number

    @property
    def name(self):
        print("getter method used")
        return self._name

    @name.setter
    def name(self, name):
        print("setter method used")
        self._name = name



student1 = Student("Rob", 1002030)
student1.name = "Robert"    #here we are accessing the setter method since we are setting a name
name1 = student1.name       #here we are accessing the getter method since we are just accessing the name variable