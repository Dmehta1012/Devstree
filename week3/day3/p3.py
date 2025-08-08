class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - ₹{self.price}")


class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"{car.make} {car.model} added to {self.name}'s inventory.")

    def remove_car(self, car):
        if car in self.inventory:
            self.inventory.remove(car)
            print(f"{car.make} {car.model} removed from inventory.")
        else:
            print("Car not found in inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("No cars in inventory.")
        else:
            print(f"{self.name} Inventory:")
            for car in self.inventory:
                car.display_info()

    def search_by_make(self, make):
        print(f"Searching for cars with make: {make}")
        found = [car for car in self.inventory if car.make.lower() == make.lower()]
        if not found:
            print("No cars found.")
        else:
            for car in found:
                car.display_info()




car1 = Car("Toyota", "Camry", 2021, 2000000)
car2 = Car("Honda", "Civic", 2022, 2500000)
car3 = Car("Toyota", "Fortuner", 2021, 4500000)
car4 = Car("Toyota", "Glanza", 2021, 1200000)

D = Dealership("SuperCars")
D.add_car(car1)
D.add_car(car2)
D.add_car(car3)
D.add_car(car4)


D.display_inventory()

D.search_by_make("Toyota")

D.remove_car(car2)

D.display_inventory()
