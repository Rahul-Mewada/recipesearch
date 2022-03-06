import Crawler as crawler
import Recipe 


def main():
    c = crawler.Crawler()
    urls = [
        "https://www.allrecipes.com/recipe/246385/jans-beer-brined-corned-beef/"
    ]
    c.crawl(urls)

if __name__ == '__main__':
    main()