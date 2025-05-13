# Base class for Vehicle
class Vehicle:
    def move(self):
        print("This vehicle moves... somehow.")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving down the road.")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying through the clouds.")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing across the water.")

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Loop through each vehicle and call move()
for v in vehicles:
    v.move()
