
# ========= > Classes and Objects < =================

# class Car:
#     # Name/Model
#     # NumberPlate
#     # No_of_seats
#     # drive (method)

#     car_tyres = 4 # class variable
 
#     def __init__ (self, name, number_plate, no_of_seats):
#         self.name = name
#         self.number_plate = number_plate
#         self.no_of_seats = no_of_seats

#     def show (self):
#         print(f"My Car name is {self.name} and its no is {self.number_plate} and no of seats in the car are {self.no_of_seats}")

#     def drive (self):
#         print(f"{self.name} is moving toward Germany")


# My_Car = Car("Toyota", 3421, 5)
# # My_Car.show()
# # My_Car.drive()
# print(My_Car.name)
# print(My_Car.car_tyres)

# My_car1 = Car("BMW", 1234, 4)
# # My_car1.show()
# # My_car1.drive()
# print(My_car1.name)
# print(My_car1.car_tyres)

# ======= > Inheritance < ============

# class Animal :
#     def speak (self):
#         print("Animal Sound")

# class Dog(Animal) :
#     def Bark (self):
#         print("Bark")

# Dog1 = Dog()
# Dog1.Bark()
# Dog1.speak()

# animal1 = Animal()
# animal1.Bark()

# ============== > Polymorphism < =============

# class Bird :
#     def make_sound (self):
#         print("Tweet")

# class Cat :
#     def make_sound (self):
#         print("Meow")

# bird1 = Bird()
# bird1.make_sound()

# cat1 = Cat()
# cat1.make_sound()

# =============> Encapsulation <=============

class BankAccount :
    def __init__(self, balance):
        self.__balance = balance

    def deposite (self, amount):
        self.__balance = self.__balance + amount

    def get_balance (self):
        print("Your Account Balance is : ", self.__balance)



person1 = BankAccount(5000)

# print(person1.__balance)
person1.get_balance()
person1.deposite(4000)
person1.get_balance()