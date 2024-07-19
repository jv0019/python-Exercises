class Person:
    def __init__(self, name="Unknown", age=0):  # Accepts name and age as optional arguments
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("XENOSIS", 5)  # Now this works because the constructor accepts name and age
person.display_details()