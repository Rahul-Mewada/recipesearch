
from unicodedata import name
import unittest


class Ingredient:
    def __init__(self, ingredient_dict):
        self.unit = None
        self.quantity = None
        for key, value in ingredient_dict.items():
            match key:
                case "name": 
                    self.name = value
                case "qty":
                    self.quantity = value
                case "unit":
                    self.unit = value
                case "input":
                    self.raw = value

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"

    def __repr__(self):
        return f"{self.name} - {self.quantity} {self.unit}"