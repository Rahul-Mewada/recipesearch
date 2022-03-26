from ast import parse
from operator import contains
from pydoc import describe
from unicodedata import category, name
import pprint as pp
from ingredient_parser import parse_ingredients
from . import author, image, rating, ingredient
import utils

class Recipe:
    
    def __init__(self, json_ld, url):
        self.image = None
        self.author = None
        self.date_published = None
        self.description = None
        self.prep_time = None
        self.cook_time = None
        self.total_time = None
        self.keywords = None
        self.servings = None
        self.category = None
        self.cuisine = None
        self.rating = None
        for key in json_ld:
            content = json_ld.get(key)
            match key:
                case "name":
                    self.name = content
                # case "image":
                #     self.image = image.Image(content)
                #     pass
                # case "author":
                #     if type(content) == list:
                #         content = content[0]
                #     if content['@type'] == 'Person':
                #         self.author = author.Author(content)
                case "datePublished":
                    self.date_published = content
                case "description":
                    self.description = content
                case "prepTime":
                    self.prep_time = content
                case "cookTime":
                    self.cook_time = content
                case "totalTime":
                    self.total_time = content
                # case "keywords":
                #     self.keywords = content
                case "recipeYield":
                    self.servings = content
                # case "recipeCategory":
                #     self.category = content
                # case "recipeCuisine":
                #     self.cuisine = content
                # case "recipeIngredient":
                #     self.ingredients = content
                # case "recipeInstructions":
                #     self.instructions = content
                # case "aggregateRating":
                #     self.rating = rating.Rating(content)
        # self.parse_instructions()
        # self.parse_ingredients()
        self.url = url
        self.url_hash = utils.crc_hash(url)

    def parse_instructions(self):
        """
        Takes the json data of instructions and parses and returns it as a list
        """
        instruction_list = []
        for instruction_dict in self.instructions:
            if instruction_dict.get('@type') == 'HowToStep':
                instruction_list.append(instruction_dict.get('text'))

        self.instructions = instruction_list
    
    def parse_ingredients(self):
        """
        Takes a list of strings of ingredients and returns a list of ingredient 
        objects
        """
        if not self.ingredients:
            print("No ingredients found")
        
        self.ingredients = utils.vulger_to_numeric(self.ingredients)

        ingredient_list = []
        ingredient_json = parse_ingredients.parse_ingredients(self.ingredients)
        for json in ingredient_json:
            cur_ingredient = ingredient.Ingredient(json)
            ingredient_list.append(cur_ingredient)

        self.ingredients = ingredient_list


    def to_json(self):
        return dict(
            name = self.name,
            date_published = self.date_published,
            description = self.description,
            prep_time = self.prep_time,
            cook_time = self.cook_time,
            total_time = self.total_time,
            servings = self.servings,
            url = dict(
                url = self.url,
                url_hash = self.url_hash
            )
        )

