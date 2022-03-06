from operator import contains
from pydoc import describe
from unicodedata import category, name
import pprint as pp


class Recipe:
    def __init__(
        self,
        name,
        image,
        author,
        datePublished,
        description,
        prepTime,
        cookTime,
        totalTime,
        keywords,
        recipeYield,
        recipeCategory,
        recipeCuisine,
        recipeIngredient,
        recipeInstructions,
        aggregateRating
    ):
        self.name = name
        self.images = image
        self.author = author
        self.date_published = datePublished
        self.description = description
        self.prep_time = prepTime
        self.cook_time = cookTime
        self.total_time = totalTime
        self.keywords = keywords
        self.servings = recipeYield
        self.category = recipeCategory
        self.cuisine = recipeCuisine
        self.ingredients = recipeIngredient
        self.instructions = recipeInstructions
        self.rating = aggregateRating # TODO: create ratings object
    
    def __init__(self, json_ld):
        for key in json_ld:
            content = json_ld.get(key)
            match key:
                case "name":
                    self.name = content
                case "image":
                    self.image = Image(content)
                case "author":
                    if content[0].get('@type') == 'Person':
                        self.author = Author(content)
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
                case "keywords":
                    self.keywords = content
                case "recipeYield":
                    self.servings = content
                case "recipeCategory":
                    self.category = content
                case "recipeCuisine":
                    self.cuisine = content
                case "recipeIngredient":
                    self.ingredients = content
                case "recipeInstructions":
                    self.instructions = content
                case "aggregateRating":
                    self.rating = content
        self.parse_instructions()
            
    def parse_instructions(self):
        """
        Takes the json data of instructions and parses and returns it as a list
        """
        instruction_list = []
        for instruction_dict in self.instructions:
            if instruction_dict.get('@type') == 'HowToStep':
                instruction_list.append(instruction_dict.get('text'))

        self.instructions = instruction_list
    

class Image:
    def __init__(self, image_dict):
        for key in image_dict:
            value = image_dict.get(key)
            match key:
                case 'description':
                    self.description = value
                case 'height':
                    self.height = value
                case 'width':
                    self.width = value
                case 'url':
                    self.url = value

class Author:
    def __init__(self, author_list):
        author_dict = author_list[0]
        for key in author_dict:
            value = author_dict.get(key)
            match key:
                case 'name':
                    self.name = value
                case 'url':
                    self.url = value