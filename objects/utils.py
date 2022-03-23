from multiprocessing.sharedctypes import Value
from urllib.parse import urlparse
import unicodedata
import binascii
from mysqlx import OperationalError

def split_url(url):
    """
    Returns the scheme domain and path from a url
    """
    parsed_seed = urlparse(url)
    scheme = parsed_seed.scheme
    domain = parsed_seed.netloc
    path = parsed_seed.path
    return (scheme, domain, path)

def generate_url(scheme, domain, path):
    """
    Returns a valid url string using the scheme, domain and path
    """
    return scheme + "://" + domain + path

def vulger_to_numeric(ingredients):
    """
    Helper function to convert unicode fractions to floats
    """
    parsed_ingredients = []
    for ingredient in ingredients:
        split_ingredients = ingredient.split(' ')
        for j, split in enumerate(split_ingredients):
            try:
                if len(split) == 1:
                    new_float = unicodedata.numeric(split)
                elif split[-1].isdigit():
                    new_float = float(split)
                else:
                    new_float = float(split[:-1]) + unicodedata.numeric(split[-1])
            except:
                continue
            if new_float:
                new_float = format(new_float, '.2f')
                split_ingredients[j] = str(new_float)

        parsed_ingredients.append(' '.join(split_ingredients))
    return parsed_ingredients

def crc_hash(url):
    data = url.encode()
    url_hash = binascii.crc32(data) & 0xffffffff
    print(url_hash)
    return url_hash