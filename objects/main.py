import crawler as crawler
import recipe 
from database import Database
import utils

def main():
    c = crawler.Crawler('https://www.foodnetwork.com/recipes', "/recipes/")
    db = Database()
    c.crawl(db)

if __name__ == '__main__':
    main()