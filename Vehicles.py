class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

object1 = Vehicle("Ford", 2007)
object2 = Vehicle("Ferrari", 2011)

object1.display_info()
object2.display_info()
