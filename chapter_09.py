
# ========= > Classes and Objects < =================

class Car:
    # Name/Model
    # NumberPlate
    # No_of_seats
    # drive (method)
    def __init__ (self, name, number_plate, no_of_seats):
        self.name = name
        self.number_plate = number_plate
        self.no_of_seats = no_of_seats

    def show (self):
        print(f"My Car name is {self.name} and its no is {self.number_plate} and no of seats in the car are {self.no_of_seats}")

    def drive (self):
        print(f"{self.name} is moving toward Germany")


My_Car = Car("Toyota", 3421, 5)
My_Car.show()
My_Car.drive()

My_car1 = Car("BMW", 1234, 4)
My_car1.show()
My_car1.drive()