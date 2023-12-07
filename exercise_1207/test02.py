class sports:
    def __init__(self, name):
        # Constructor for the sports class
        self._name = name

    @property
    def sports_name(self):
        # Getter method for the sports name
        return self._name
    
    @sports_name.setter
    def sports_name(self, value):
        # Setter method for the sports name
        self._name = value

    def practice(self):
        # Method to simulate sport practice
        print("Doing sport practice")

class Landsport(sports):
    def __init__(self, name, field):
        # Constructor for the Landsport class, inheriting from sports
        super().__init__(name)
        self._field = field
    
    @property
    def landsports_field(self):
        # Getter method for the landsport field
        return self._field

    def practice(self):
        # Method to simulate land sport practice
        print("Doing land sport practice")

class WaterSports(sports):
    def __init__(self, name, activity):
        # Constructor for the WaterSports class, inheriting from sports
        super().__init__(name)
        self._activity = activity

    @property
    def watersport_activity(self):
        # Getter method for the watersport activity
        return self._activity

    def practice(self):
        # Method to simulate water sport practice
        print("Doing water sport practice")

# Creating an instance of Landsport
baseball = Landsport("baseball", "baseball field")
print(baseball.sports_name)
print(baseball.landsports_field)
print(baseball.practice())  # Using the practice method from the Landsport class

# Creating an instance of WaterSports
water_skiing = WaterSports("Water_skiing", "Strap on your skis and fly across the water")
print(water_skiing.sports_name)
print(water_skiing.watersport_activity)
print(water_skiing.practice())  # Using the practice method from the WaterSports class

# Creating an instance of sports
golf = sports("golf")
print(golf.sports_name)
print(golf.practice())  # Using the practice method from the base sports class
