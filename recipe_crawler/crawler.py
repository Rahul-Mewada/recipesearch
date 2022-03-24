import extruct as ex
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pprint as pp
from models import recipe as r
import utils
from urllib.robotparser import RobotFileParser
from selenium.webdriver.common.by import By
import time
import urllib

class Crawler:
    def __init__(self, seed_url, path_constraint):
        self.seed_url = seed_url
        self.scheme, self.domain, self.path = utils.split_url(seed_url)
        self.robot_parser = RobotFileParser()
        self.robot_parser.set_url(utils.generate_url(self.scheme, self.domain, '/robots.txt'))
        self.robot_parser.read()
        self.visited_sites = set()
        self.path_constraint = path_constraint
    
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

    def get_valid_urls(self, driver, source):
        """
        Returns all valid urls from an html source.
        """
        print("Getting valid urls")
        if not source:
            print("Couldn't get urls from source")
            return None
        web_elements = driver.find_elements(By.TAG_NAME, 'a')
        urls = []
        for web_element in web_elements:
            link = web_element.get_attribute("href")
            if link:
                link_scheme, link_domain, link_path = utils.split_url(link)
                if self.valid_link(link_scheme, link_domain, link_path):
                    urls.append(link)
        return urls
    
    def valid_link(self, link_scheme, link_domain, link_path):
        """
        Returns true if a link is valid. Checks if a link is not blocked by robots.txt and if it has
        the same domain as the seed url's domain.
        """
        link = utils.generate_url(link_scheme, link_domain, link_path)
        print(link)
        print(self.robot_parser.can_fetch("*", link))
        if self.robot_parser.can_fetch("*", link) and link_domain == self.domain \
            and self.in_path(link_path) and not link in self.visited_sites:
            return True
        return False
            
    def in_path(self, link_path):
        """
        Return true if the seed_path is in the link_path
        """
        link_split = link_path.split('/')
        constraint_split = self.path_constraint.split('/')
        return link_split[1] == constraint_split[1]

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
                
    def return_recipe(self, driver, source, url):
        """
        Returns a recipe object from a particular url
        """
        if not source:
            print("Couldnt extract HTML from " + url)
            return None
        json_ld = self.get_json(source)
        recipe_json_ld = self.search_for_recipe(json_ld)
        if not recipe_json_ld:
            print('Couldnt extract recipe from json-ld')
            return None
        print('Creating recipe object')
        recipe = r.Recipe(recipe_json_ld, url)
        return recipe

    def crawl(self, database):
        """
        Initiates a bfs from the seed_url and crawls all valid neighboring urls while storing 
        recipies into the database. 
        """
        driver = self.get_driver()
        to_visit = []
        to_visit.append(self.seed_url)
        count = 0
        while to_visit and count < 10:
            start_time = time.time()
            cur_url = to_visit.pop()
            cur_source = self.get_source(driver, cur_url)
            recipe = self.return_recipe(driver, cur_source, cur_url)
            self.visited_sites.add(cur_url)
            if recipe:
                database.insert_recipe(recipe)
            cur_neighbors = self.get_valid_urls(driver, cur_source)
            for neighbor in cur_neighbors:
                to_visit.append(neighbor)
            end_time = time.time()
            if self.robot_parser.crawl_delay("*") and end_time - start_time < self.robot_parser.crawl_delay("*"):
                time.sleep(end_time - start_time)
            count += 1
        
    def get_recipe(self, url):
        driver = self.get_driver()
        source = self.get_source(driver, url)
        return self.return_recipe(driver, source, url)

    def get_recipe_json(self, url):
        driver = self.get_driver()
        source = self.get_source(driver, url)
        json_ld = self.get_json(source)
        return self.search_for_recipe(json_ld)