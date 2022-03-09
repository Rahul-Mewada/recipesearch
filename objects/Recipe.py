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
    
    def __init__(self, json_ld, url):
        self.prep_time = None
        self.cook_time = None
        self.total_time = None
        self.keywords = None
        self.description = None
        self.servings = None
        self.category = None
        self.cuisine = None
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
                    self.rating = Rating(content)
        self.parse_instructions()
        self.url = url
            
    def parse_instructions(self):
        """
        Takes the json data of instructions and parses and returns it as a list
        """
        instruction_list = []
        for instruction_dict in self.instructions:
            if instruction_dict.get('@type') == 'HowToStep':
                instruction_list.append(instruction_dict.get('text'))

        self.instructions = instruction_list
    
    def return_list_to_string(self, string_list):
        """
        Helper function to condense a list of strings to a single string seperated by *
        """
        if type(string_list) == str:
            return string_list
        elif type(string_list) == list:
            return_string = ""
            for element in string_list:
                return_string += element + "*"
            print(return_string)
            return return_string

    def to_sql(self):
        """
        Helper function to input Recipe into sql args
        """
        sql_args = (
            self.name,
            self.image.description,
            self.image.height,
            self.image.width,
            self.image.url,
            self.author.name,
            self.author.url,
            self.date_published,
            self.description,
            self.prep_time,
            self.cook_time,
            self.total_time,
            self.return_list_to_string(self.keywords),
            self.servings,
            self.return_list_to_string(self.category),
            self.return_list_to_string(self.cuisine),
            self.return_list_to_string(self.ingredients),
            self.return_list_to_string(self.instructions),
            self.rating.count,
            self.rating.value
        )
        return sql_args

class Image:
    def __init__(self, image_dict):
        self.description = None
        self.height = None
        self.width = None
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


class Rating:
    def __init__(self, rating_dict):
        self.count = None
        self.value = None
        if rating_dict.get('@type') == 'AggregateRating':
            for key in rating_dict:
                value = rating_dict.get(key)
                match key:
                    case 'ratingCount':
                        self.count = value
                    case 'ratingValue':
                        self.value = value
