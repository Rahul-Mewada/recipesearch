class Rating:
    def __init__(self, rating_dict):
        self.count = None
        self.value = None
        if rating_dict.get('@type') == 'AggregateRating':
            for key in rating_dict:
                value = rating_dict.get(key)
                match key:
                    case 'ratingCount':
                        self.count = value
                    case 'ratingValue':
                        self.value = value
