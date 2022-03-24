
class Author:
    def __init__(self, author_list):
        author_dict = author_list
        for key in author_dict:
            value = author_dict.get(key)
            match key:
                case 'name':
                    self.name = value
                case 'url':
                    self.url = value

    def __str__(self):
        return f"Author name: {self.name} \nAuthor url: {self.url}"
    
    def __repr__(self) -> str:
        return f"Author name: {self.name} \nAuthor url: {self.url}"