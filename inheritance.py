class Parent:
    def __init__(self, last_name, eye_color):
        print("The Parent constructor is called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("The Child constructor is called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

#bily_John = Parent("Bily", "blue")

#print(bily_John.last_name)
#print(bily_John.eye_color)

moraia_John = Child("Moraia","John",5)
print(moraia_John.last_name)
print(moraia_John.eye_color)
print(moraia_John.number_of_toys)
