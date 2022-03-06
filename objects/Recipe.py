from pydoc import describe
from unicodedata import category
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
                    self.image = content
                case "author":
                    self.author = content
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

    def parse_fields(self):
        pass
            
   