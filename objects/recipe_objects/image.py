
class Image:
    def __init__(self, image_dict):
        self.height = None
        self.width = None
        self.description = None
        for key in image_dict:
            value = image_dict.get(key)
            match key:
                case 'description':
                    self.description = value
                case 'height':
                    self.height = value
                case 'width':
                    self.width = value
                case 'url':
                    self.url = value

    def __str__(self):
        return f"Image url: {self.url} \nImage description: {self.description} \nHeight: {self.height} Width: {self.width}"
    
    def __repr__(self) -> str:
        return f"Image url: {self.url} \nImage description: {self.description} \nHeight: {self.height} Width: {self.width}"