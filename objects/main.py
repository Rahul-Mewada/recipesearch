import crawler as crawler
import recipe 
from database import Database

def main():
    c = crawler.Crawler('https://www.allrecipes.com/recipes/')
    db = Database()
    c.crawl(db)

if __name__ == '__main__':
    main()