'''
chapter 9
classes
'''
class Dog():
  """A simple attempt too model a dog."""

  def__init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age

  def sit(self):
    """Simulate a dog sitting in response to a coommand."""
    print(self.name.title() + " is now sitting.")

  def roll_over(self):
    """Simulate rolling over in response to a comand."""
    print(self.name.title() + " rolled over!")

my_dog - Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)

#classes and instances
class Car():
  """A simple attempt to represent a car."""

  def__init__(self, make, model, year):
    """Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

  def read_odometer(self):
    """Print a statement showing the car's mileage."""
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    """Set the odometer reading to the given value."""
    self.odometer)_reading = mileage
    """
    Set the odometer reading to the given value.
    Reject the change if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increment_odometer(self, miles)
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print (my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#__init__() method
class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""

  def __init__(self, make, model, year):
    """Initializes attributes of the parent class."""
    super().__init__(make, model, year)
    self.battery_size = 70
    self.battery = Battery()

  def describe_battery(self):
    """Print statement describing battery size."""
    print("This car has a " + str(self.battery_size) + "-kWh battery.")

  def fill_gas_tank(self):
    print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

#defining attributes/methods for child class
my_tesla.describe_battery()

#instances as attributes
class Battery():
  """A simple attempt to model a battery for an electric car."""

  def __init__(self, battery_size=70):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size

  def describe_battery(self):
    """Prints a statement describing the battery size."""
    print("This car has a " + str(self.battery_size) + "-kWh battery.")

  def get_range(self):
    #Print a statement about the range this battery provides.
    if self.battery_size == 70"
      range = 240
    elif self.battery_size == 85:
      range = 270

    message = "This car can go approximately " + str(range)
    message += " miles on a full charge."
    print(message)

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#importing multiple classes from a module
from car, import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
