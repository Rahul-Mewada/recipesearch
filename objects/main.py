import Crawler as crawler
import Recipe 
from Database import Database

def main():
    c = crawler.Crawler()
    urls = [
        "https://www.foodnetwork.com/recipes/food-network-kitchen/15-minute-tofu-and-vegetable-stir-fry-3676440"
    ]
    db = Database()
    c.crawl(urls, db)
    db.print_entries()

if __name__ == '__main__':
    main()