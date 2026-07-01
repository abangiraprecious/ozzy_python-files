# create the class - blueprint
class Boda:
    def __init__(self, driver, plate, fuel): #parementers
        self.driver = driver #self refers to the object being built. So this means "store the driver value on this particular object."
        self.plate = plate #self is the object itself, and it always refrs to whatever is sitting before the dot when method gets called
        self.fuel = fuel
    def start(self):
        print(f"{self.driver} has started the boda {self.plate}")

    def ride(self, distance):
        self.fuel = self.fuel - distance
        print(f"Rode {distance} km. fuel remaining {self.fuel}")

#object   
boda1 = Boda("John", "UAA 123A", 50)
# boda2 = Boda("Gad", "UAN 765D")

# print(boda1.plate)

boda1.start()
boda1.ride(10)
boda1.ride(15)