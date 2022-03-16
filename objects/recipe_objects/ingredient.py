
class Ingredient:
    def __init__(self, ingredient_dict):
        self.name = None
        self.unit = None
        self.quantity = None
        self.name = ingredient_dict["name"]
        self.quantity = ingredient_dict["qty"]
        self.unit = ingredient_dict["unit"]