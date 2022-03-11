import crawler as crawler
import recipe 
from database import Database
import utils

def main():
    c = crawler.Crawler('https://www.allrecipes.com/recipes/', "/recipe/")
    db = Database()
    c.crawl(db)

if __name__ == '__main__':
    main()