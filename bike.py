from factory import *

class bike(factory):

    def __init__(self, fuel_type = 'Petrol'):
        super().__init__()
        self.wheels = 2
        self.seats = 2
        self.fuel_type = fuel_type 
    
    def head_light(self, on_or_off = "off"):
 
        if(self.state == 1): # If Bike is turned on then only turn on the lights

            hd = on_or_off
        
            if(hd.lower() == "on"):
                print("Head light is truned on")
            elif(hd.lower() == "off"):
                print("Head light is truned off")

        else:
            print("Bikes Power Supply is off, Please turn on the Bike")


    def re_fuel(self):
        if(self.fuel_type.lower() == "electric"):
            print("Charging the Bike.....")
        else:
            print(f"Refueled with {self.fuel_type}")




