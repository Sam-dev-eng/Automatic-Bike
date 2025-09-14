
class Bike:
    def __init__(self):
        self.isOn = False
        self.acceleration = 0
        self.gear = 0

    def start(self):
        self.isOn = True

    def stop(self):
        self.isOn = False

    def power(self):
        if self.isOn:
            return "Power on"
        else:
            return "Power off"

    def set_gear(self):
        if self.isOn == True and self.gear == 0:
            self.gear+=1

    def check_gear(self):
        return self.gear

    def accelerate(self):

        if self.isOn and self.gear > 0 and self.acceleration + self.gear <= 123:
            self.acceleration +=  self.gear
            if self.acceleration > 20 and self.gear == 1:
                self.gear += 1
            elif self.acceleration > 30 and self.gear == 2:
                self.gear += 1
            elif self.acceleration > 40 and self.gear == 3:
                self.gear += 1
        return

    def check_acceleration(self):
        return self.acceleration

    def decelerate(self):
        if self.isOn and self.gear > 0:
            self.acceleration -= self.gear
            if self.acceleration < 41 and self.gear == 4:
                self.gear -= 1
            elif self.acceleration < 31 and self.gear == 3:
                self.gear -= 1
            elif self.acceleration < 21 and self.gear == 2:
                 self.gear -= 1
            elif self.acceleration == 0 and self.gear == 1:
                self.gear -= 1



