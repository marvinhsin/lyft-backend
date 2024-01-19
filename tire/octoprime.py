from tire.tire import Tire

class Octoprime(Tire):
    def __init__(self, sensors):
        self.sensors = sensors
    
    def needs_service(self):
        if sum(self.sensors) >= 3:
            return True
        return False