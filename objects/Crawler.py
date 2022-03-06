import extruct as ex
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pprint as pp
import Recipe as r

class Crawler:
    def __init__(self):
        pass

    def get_driver(self):
        """
        Creates and returns a chrome web driver
        """
        print('Creating driver')
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options = options)
        return driver

    def get_source(self, driver, url) -> str:
        """
        Uses the driver to return the HTML from a particular url
        """
        print('Getting source from ' + url)
        driver.get(url)
        return driver.page_source

    def get_json(self, source):
        """
        Extracts and returns the json data from an HTML file
        """
        print('Extracting json from source')
        return ex.extract(source, syntaxes=['json-ld'])

    def search_for_recipe(self, json_ld):
        """
        Searches the json-ld data for a recipe json and returns it
        """
        print("Searching for recipes in json-ld")
        queue = []
        cur_ele = json_ld
        queue.append(cur_ele)
        while queue:
            cur_ele = queue.pop(0)
            if type(cur_ele) is dict:
                if cur_ele.get('@type') == 'Recipe':
                    return cur_ele 
                for keys in cur_ele:
                    content = cur_ele.get(keys)
                    if(type(content) is list) or (type(content) is dict):
                        queue.append(content)
            elif type(cur_ele) is list:
                for ele in cur_ele:
                    if(type(ele) is list) or (type(ele) is dict):
                        queue.append(ele)
        return None
                
    def return_recipe(self, url):
        """
        Returns a recipe object from a particular url
        """
        driver = self.get_driver()
        source = self.get_source(driver, url)
        if not source:
            print("Couldnt extract HTML from " + url)
            return None
        json_ld = self.get_json(source)
        recipe_json_ld = self.search_for_recipe(json_ld)
        if not recipe_json_ld:
            print('Couldnt extract recipe from json-ld')
            return None
        print('Creating recipe object')
        recipe = r.Recipe(recipe_json_ld)
        pp.pprint(vars(recipe))
        print()
        return recipe

    def crawl(self, urls):
        """
        Returns a list of recipes from a list of urls
        """
        recipes = []
        for url in urls:
            recipe = self.return_recipe(url)
            if recipe:
                recipes.append(recipe)
        return recipes