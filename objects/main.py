from multiprocessing.sharedctypes import Value
from re import A
import crawler as crawler
from recipe_objects import recipe, image, author, ingredient, rating
from database import Database
import utils
from test import TestDumper
import redis
import pprint as pp
import unicodedata

def main():
    # c = crawler.Crawler('https://www.foodnetwork.com/recipes', "/recipes/")
    # db = Database()
    # c.get_recipe("https://www.allrecipes.com/recipe/213826/best-ever-irish-soda-bread/")
    url_list = [
        "https://www.allrecipes.com/recipe/278882/triple-chocolate-chunk-cookies/",
        "https://www.allrecipes.com/recipe/10782/birds-nests-iii/",
        "https://www.allrecipes.com/recipe/230279/divine-macaroons/",
        "https://www.allrecipes.com/recipe/242366/easy-chewy-flourless-peanut-butter-cookies/",
        "https://www.allrecipes.com/recipe/277492/slow-cooker-vegan-leek-and-potato-soup/",
        "https://www.allrecipes.com/recipe/276451/slow-cooker-turkey-meatballs-in-tomato-sauce/",
        "https://www.allrecipes.com/recipe/256610/grandmas-hungarian-stuffed-cabbage-slow-cooker-variation/",
        "https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/"
    ]
    conn = redis.Redis(host='localhost')
    td = TestDumper(url_list, conn)
    json_list = td.get_jsons()
    recipies = []
    for recipe_json in json_list:
        recipies.append(recipe.Recipe(recipe_json, url_list[0]))

    
    
if __name__ == '__main__':
    main()