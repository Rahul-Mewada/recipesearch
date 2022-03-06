import Crawler as crawler
import Recipe 


def main():
    c = crawler.Crawler()
    urls = [
        "https://www.foodnetwork.com/recipes/food-network-kitchen/15-minute-tofu-and-vegetable-stir-fry-3676440"
    ]
    c.crawl(urls)

if __name__ == '__main__':
    main()