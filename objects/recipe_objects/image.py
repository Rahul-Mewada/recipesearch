
class Image:
    def __init__(self, image_dict):
        self.description = None
        self.height = None
        self.width = None
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
