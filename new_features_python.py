# version 13.3 Python

# usar Optional
from typing import Optional

class Address:
  def __init__(self, street: str, postcode:str) -> None:
    self.street = street
    self.postcode = postcode

class Person:
  def __init__(self, firstname: str, lastname: str, age: int, address: Optional[Address]= None) -> None:
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.address = address
    

my_address = Address("123 Main St", "NH1234")

me = Person("Jon", "Smith", 21, my_address)

print(me.firstname)
print(me.address.street)

