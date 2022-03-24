from multiprocessing.sharedctypes import Value
from re import A
import crawler as crawler
from models import recipe, image, author, ingredient, rating
import utils
from test import TestDumper
import redis
import pprint as pp
import unicodedata
import utils

def main():
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
    for url in url_list:
        utils.crc_hash(url)
    
if __name__ == '__main__':
    main()