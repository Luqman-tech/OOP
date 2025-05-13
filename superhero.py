# Base class for a generic Superhero
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I'm {self.name} from {self.origin}, and my power is {self.power}!")

# Subclass for a FlyingSuperhero (Inheritance example)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

# Another subclass for a SpeedsterSuperhero
class SpeedsterSuperhero(Superhero):
    def __init__(self, name, power, origin, run_speed):
        super().__init__(name, power, origin)
        self.run_speed = run_speed

    def run(self):
        print(f"{self.name} is running at {self.run_speed} km/h!")

# Create objects
ironwing = FlyingSuperhero("Ironwing", "Laser Vision", "Sky City", 800)
blazestrike = SpeedsterSuperhero("Blazestrike", "Super Speed", "Metroville", 1200)

# Call methods
ironwing.introduce()
ironwing.fly()

blazestrike.introduce()
blazestrike.run()
