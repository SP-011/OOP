from factory import *

class car(factory):

    def __init__(self):
        super().__init__()
        
        self.wheels = 4
        self.seat = 7
        self.doors = 5

    def ac(self, on_or_off = "on"):

        if(self.state == 1): # If Car is turned on then only start the ac
            nf = on_or_off

            if(nf.lower() == "on"):
                print("Turning on Air Conditioner")
            elif(nf.lower() == "off"):
                print("Air Conditioner turned off")
        else:
            print("Car Power is off, Please turn  on the Car")


    def gear(self, gear_type):
        if(type(gear_type) == int  and gear_type <= 5): # If Gear is Integer and less than 5 then only start the gear will set for Forward direction

            print("Setting on gear {}".format(gear_type))

        elif(gear_type.lower() == "r" or gear_type.lower() == "reverse"): # If Gear is 'r' or 'reverse' then only the gear will set for Reverse direction

            print("On Reverse Gear...")

        else: # Or else Invallid Gear Value
            print("Invalid Gear Type")

    

