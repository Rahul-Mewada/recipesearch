
class Image:
    def __init__(self, image_dict):
        self.height = None
        self.width = None
        self.caption = None
        for key in image_dict:
            value = image_dict.get(key)
            match key:
                case 'caption':
                    self.caption = value
                case 'height':
                    self.height = value
                case 'width':
                    self.width = value
                case 'url':
                    self.url = value

    def __str__(self):
        return self.url
    
    def __repr__(self) -> str:
        return self.url

    def to_json(self):
        return dict(
            height = self.height,
            width = self.width,
            caption = self.caption,
            url = self.url
        )