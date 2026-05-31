class Task:
    x = 5
    def __init__(self,downtime:int):
        self.downtime = downtime
    
    
    def __lt__(self, other:"Task"):
        if self.downtime < other.downtime:
            return other
        return self
    
    def __repr__(self)->str:
        return f"Task downtime = {self.downtime}"
    
    
    
class Person:
    def __init__(self,name):
        self.name = name
        self = self