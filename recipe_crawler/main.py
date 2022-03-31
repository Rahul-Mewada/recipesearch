from multiprocessing.sharedctypes import Value
from re import A
from crawler import Crawler
from models import recipe, image, author, ingredient, rating
import utils
import redis
import pprint as pp
import unicodedata
import utils
from client import Client
from json import dumps
import yake

def main():
    url_list = [
        "https://www.allrecipes.com/",
        "https://www.allrecipes.com/recipe/278882/triple-chocolate-chunk-cookies/",
        "https://www.allrecipes.com/recipe/10782/birds-nests-iii/",
        "https://www.allrecipes.com/recipe/230279/divine-macaroons/",
        "https://www.allrecipes.com/recipe/242366/easy-chewy-flourless-peanut-butter-cookies/",
        "https://www.allrecipes.com/recipe/277492/slow-cooker-vegan-leek-and-potato-soup/",
        "https://www.allrecipes.com/recipe/10782/birds-nests-iii/",
        "https://www.allrecipes.com/recipe/276451/slow-cooker-turkey-meatballs-in-tomato-sauce/",
        "https://www.allrecipes.com/recipe/256610/grandmas-hungarian-stuffed-cabbage-slow-cooker-variation/",
        "https://www.allrecipes.com/recipe/230279/divine-macaroons/",
        "https://www.allrecipes.com/recipes/78/breakfast-and-brunch/",
        "https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/",
        "https://www.allrecipes.com/recipe/79470/simple-scones/",
        "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/",
        "https://www.allrecipes.com/recipe/9870/easy-sugar-cookies/",
        "https://www.allrecipes.com/recipe/10687/mrs-siggs-snickerdoodles/",
        "https://www.allrecipes.com/recipe/278882/triple-chocolate-chunk-cookies/",
        "https://www.allrecipes.com/"
    ]
    client = Client('http://localhost:8000/api/')
    crawl = Crawler('https://www.allrecipes.com', '/recipe', client)
    
    crawl.crawl_urls(url_list)
    # crawl.get_recipies(url_list)



if __name__ == '__main__':
    main()