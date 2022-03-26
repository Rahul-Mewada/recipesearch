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

def main():
    # url_list = [
    #     "https://www.allrecipes.com/recipe/278882/triple-chocolate-chunk-cookies/",
    #     "https://www.allrecipes.com/recipe/10782/birds-nests-iii/",
    #     "https://www.allrecipes.com/recipe/230279/divine-macaroons/",
    #     "https://www.allrecipes.com/recipe/242366/easy-chewy-flourless-peanut-butter-cookies/",
    #     "https://www.allrecipes.com/recipe/277492/slow-cooker-vegan-leek-and-potato-soup/",
    #     "https://www.allrecipes.com/recipe/276451/slow-cooker-turkey-meatballs-in-tomato-sauce/",
    #     "https://www.allrecipes.com/recipe/256610/grandmas-hungarian-stuffed-cabbage-slow-cooker-variation/",
    #     "https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/"
    # ]
    print("Generated Hashes")
    print()
    url_list = [
        "https://www.allrecipes.com/recipe/278882/triple-chocolate-chunk-cookies/",
        "https://www.allrecipes.com/recipe/10782/birds-nests-iii/",
        "https://www.youtube.com",
        "https://www.news.com",
        "https://www.allrecipies.com/"
    ]
    # crawl = Crawler('https://www.allrecipes.com', '/recipe')
    client = Client('http://localhost:8000/api/')
    
    for url in url_list:
        client.is_visited(url)

if __name__ == '__main__':
    main()