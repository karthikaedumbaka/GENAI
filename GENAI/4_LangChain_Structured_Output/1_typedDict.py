from typing import TypedDict

class Pesron(TypedDict):
    names : str 
    age:int

new_preson : Pesron = {'names':"karthik", "age": 24}
print(new_preson)