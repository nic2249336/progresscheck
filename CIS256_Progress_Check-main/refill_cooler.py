"""
Nicholas Triggs
Module 01 Programming Project Part B

This program uses a class to find info on water cooler using PEP 8 standers for the code.
"""


class Cooler:
    def __init__(self, location, remaining_water):
        self.location = location
        self.remaining_water = remaining_water

    def bottle_fill(self):
        if self.remaining_water <= 0:
            print("empty please refill!")
        else:
            self.remaining_water = self.remaining_water - 0.5

    def refill_cooler(self):
        self.remaining_water = 20
        print(f"The cooler has been refilled to 20 gallons")

    def cooler_location(self):
        self.location = input(f"Where is the cooler now: ")

    def end_of_day(self):
        print(
            f"The cooler is at {self.location} and has {self.remaining_water} gallons left."
        )


Cooler_1 = Cooler("Break-room", 2)
Cooler_1.bottle_fill()
Cooler_1.bottle_fill()
Cooler_1.bottle_fill()
Cooler_1.bottle_fill()
Cooler_1.bottle_fill()
Cooler_1.refill_cooler()
Cooler_1.bottle_fill()
Cooler_1.bottle_fill()
Cooler_1.end_of_day()

Cooler_2 = Cooler("Meeting room", 12)
Cooler_2.bottle_fill()
Cooler_2.cooler_location()
Cooler_2.bottle_fill()
Cooler_2.bottle_fill()
Cooler_2.end_of_day()
