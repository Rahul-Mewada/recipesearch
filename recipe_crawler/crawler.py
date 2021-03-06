import extruct as ex
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pprint as pp
from models import recipe as r
import utils
from urllib.robotparser import RobotFileParser
from selenium.webdriver.common.by import By
import time
import validators
from w3lib.url import url_query_cleaner
from bs4 import BeautifulSoup
class Crawler:
    def __init__(self, seed_url, path_constraint, client):
        self.seed_url = seed_url
        self.scheme, self.domain, self.path = utils.split_url(seed_url)
        self.robot_parser = RobotFileParser()
        self.robot_parser.set_url(utils.generate_url(self.scheme, self.domain, '/robots.txt'))
        self.robot_parser.read()
        self.path_constraint = path_constraint
        self.driver = self._get_driver()
        self.client = client

    def _get_driver(self):
        """
        Creates and returns a chrome web driver
        """
        print('Creating driver')
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options = options)
        return driver

    def _get_source(self, url) -> str:
        """
        Uses the driver to return the HTML from a particular url
        """
        print('Getting source from ' + url)
        self.driver.get(url)
        return self.driver.page_source

    def _get_json(self, source):
        """
        Extracts and returns the json data from an HTML file
        """
        print('Extracting json from source')
        return ex.extract(source, syntaxes=['json-ld'])

    def _get_valid_urls(self, source):
        """
        Returns all valid urls from an html source.
        """
        print("Getting valid urls")
        if not source:
            print("Couldn't get urls from source")
            return None
        soup = BeautifulSoup(source, 'html.parser')
        elements = soup.find_all("a")
        time.sleep(1)
        url_list = []
        for element in elements:
            url = element.get('href')
            if url and self._is_valid(url):
                url_list.append(url)
        return url_list
    
    def _is_valid(self, url):
        """
        Returns true if a link is valid. Checks if a link is not blocked by robots.txt and if it has
        the same domain as the seed url's domain.
        """
        if type(url) != str or not validators.url(url):
            return False
        url_scheme, url_domain, url_path = utils.split_url(url)
        if self.robot_parser.can_fetch("*", url) and url_domain == self.domain \
            and self._in_path(url_path):
            return True
        return False

    def _in_path(self, link_path):
        """
        Return true if the seed_path is in the link_path
        """
        if not link_path:
            return False
        link_split = link_path.split('/')
        constraint_split = self.path_constraint.split('/')
        return link_split[1] == constraint_split[1]

    def _search_for_recipe(self, json_ld):
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
                
    def _return_recipe(self, source, url):
        """
        Returns a recipe object from a particular url
        """
        if not source:
            print("Couldnt extract HTML from " + url)
            return None
        json_ld = self._get_json(source)
        recipe_json_ld = self._search_for_recipe(json_ld)
        if not recipe_json_ld:
            print('Couldnt extract recipe from json-ld')
            return None
        print('Creating recipe object')
        recipe = r.Recipe(recipe_json_ld, url)
        return recipe

    def crawl_urls(self, url_list):
        """
        Crawls the list of urls and returns a list of scraped recipes if they exist
        """
        recipe_list = []
        crawl_delay = self.robot_parser.crawl_delay("*")
        for url in url_list:
            is_valid, is_visited = self._is_valid(url)
            if is_valid:
                start_time = time.time()  
                source = self._get_source(url)
                recipe = self._return_recipe(source, url)
                if recipe:
                    self.client.add_recipe(recipe)
                elif not is_visited:
                    self.client.add_url(url)
                end_time = time.time()
                if crawl_delay and end_time - start_time < crawl_delay:
                    time.sleep(crawl_delay - (end_time - start_time))
            elif not is_visited:
                self.client.add_url(url)

    def crawl(self):
        """
        Initiates a bfs from the seed_url and crawls all valid neighboring urls while storing 
        recipies into the database. 
        """
        to_visit = []
        crawl_delay = self.robot_parser.crawl_delay("*")
        to_visit.append(self.seed_url)
        global_time = time.time()
        count = 0
        while to_visit and count < 100:
            print()
            url = to_visit.pop()
            if self.client.is_visited(url):
                continue
            start_time = time.time()
            source = self._get_source(url)
            recipe = self._return_recipe(source, url)
            neighbors = self._get_valid_urls(source)
            end_time = time.time()

            for neighbor in neighbors:
                to_visit.append(url_query_cleaner(neighbor, remove=True)) 

            if recipe:
                print("Saving Recipe")
                self.client.add_recipe(recipe)
            elif url != self.seed_url:
                print("Saving url")
                self.client.add_url(url)
            
            if crawl_delay and end_time - start_time < crawl_delay:
                time.sleep(crawl_delay - (end_time - start_time))
            print()
