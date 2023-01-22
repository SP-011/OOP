
class factory:
    def __init__(self):
        self.fuel_type = "Petrol"
        self.wheels = None
        self.engine = "1cc"
        self.state = 0

    def run(self):
        self.state = 1
        print("Starting the engine...")

    def stop(self):
        self.state = 0
        print("Stopping the engine...")

    

