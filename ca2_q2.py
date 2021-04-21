# date : 11/01/2021
# Author : Renato Gusani
# Student no. : x19411076
# Question 2 – OOP & Testing : a2, b2

# * * * * * * * * * * question a.2) * * * * * * * * * *

import pytest
import re
from pytest import raises

class Product:
  # constructor method
  def __init__(self, product_id, name, cost):
    self.product_id = product_id
    if name > 50:
        raise NameError("Name must be under 50 characters, was %s." % name)
    else:
        self.name = name
        self.cost = cost

# Testing the above with pytest


class MyTestClass:
def product_id(self):
assert True
def name(self):
assert True
def cost(self):
assert True


# * * * * * * * * * * question b.2) * * * * * * * * * *


class Person(Contact):
  # constructor method
  def __init__(self, name, phone_number, email_address):
    self.name = name
    self.phone_number = phone_number
    self.email_address = email_address

# making 4 contacts
name = ["james", "john", "rambo", "arnie"]
phone_number = [123456789, 987654321, 13579865, 987612345]
email_address = ["john@email.com", "james@email.com", "rambo@email.com", "arnie@email.com"]

class Address(Contact):
  # constructor method
  def __init__(self, street, city, country):
    self.street = street
    self.city = city
    self.country = country

street = ["elm", "ave", "north", "strand"]
city = ["nyc", "miami", "colorado", "sputnik"]
country = ["city1", "city2", "city3", "city4"]

class Contact(Person, Address):
    pass

class Notebook(Contact):
  # constructor method
  def __init__(self, name, contact):
    self.name = name
    self.contact = []

