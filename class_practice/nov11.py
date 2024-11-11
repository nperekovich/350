#create vehicle class
class Vehicle:

    #defines vehicle parameters
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

#create bus 'object'
class Bus(Vehicle):
    pass #passes vehicle parameters onto bus object

#attributes of bus
School_bus = Bus("Volvo", 180, 12)

#prints bus details
print("Name of Bus:",  School_bus.name,  
      "Maximum Speed:",  School_bus.max_speed,  
      "Mileage:",  School_bus.mileage)
