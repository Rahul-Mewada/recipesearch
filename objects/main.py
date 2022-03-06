import Crawler as crawler
import Recipe 


def main():
    c = crawler.Crawler()
    urls = [
        'https://www.foodnetwork.com/recipes/rachael-ray/fish-fry-recipe-1939977'
    ]
    c.crawl(urls)

if __name__ == '__main__':
    main()