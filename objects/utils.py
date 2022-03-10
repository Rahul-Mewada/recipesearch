from urllib.parse import urlparse

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