class Vehicle:

    def __init__(self, brand, speed):
       
        self.__brand = brand
        self.__speed = speed

    
    def get_brand(self):
        return self.__brand

    def get_speed(self):
        return self.__speed

    
    def display_info(self):
        print("Brand:", self.__brand)
        print("Speed:", self.__speed, "km/h")



class Car(Vehicle):

    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

   
    def fuel_type(self):
        print("Fuel Type: Petrol")

    def display_car(self):
        self.display_info()
        print("Seats:", self.seats)


class Bike(Vehicle):

    def __init__(self, brand, speed, helmet_required):
        super().__init__(brand, speed)
        self.helmet_required = helmet_required

   
    def fuel_type(self):
        print("Fuel Type: Electric")

    def display_bike(self):
        self.display_info()
        print("Helmet Required:", self.helmet_required)



car1 = Car("Toyota", 180, 5)
bike1 = Bike("Tesla Bike", 120, True)


print("----- Car Details -----")
car1.display_car()
car1.fuel_type()

print("\n----- Bike Details -----")
bike1.display_bike()
bike1.fuel_type()