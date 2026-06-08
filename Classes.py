class Task:
    x = 5
    def __init__(self,downtime:int):
        self.downtime = downtime
        
    
    def __lt__(self, other:"Task"):
        if self.downtime < other.downtime:
            return other
        return self
    
    
    def weather_delay(self, delay_period):
        self.downtime += delay_period
        return self.dowmtime
    
    
    def __repr__(self)->str:
        return f"Task downtime = {self.downtime}"
    
    
    
class Person:
    def __init__(self, name, country, city, age = 0):
        self.name = name
        self.country = country
        self.city = city
        self.age = age
        
        
    def aging(self, years):
        self.age += years
        return self.age
    
    
    def greet(self):
        print("Hello" + self.name)
        
    
class Car:
    def __init__(self, colour:str, brand:str, model:str, displ:float, mileage:float, drive:str, age = 0):
        self.colour = colour
        self.brand = brand
        self.model = model
        self.displ = displ
        self.mileage = mileage
        self.drive = drive
        self.age = age
        
    def display_info(self):
        print(f"{self.colour},{self.brand},{self.model},{self.displ},{self.age}")
        
    def add_turbo():
        return
        
    def engine_swap():
        return
        
    def wrap_colour():
        return
        
    def add_mileage():
        return
        
        