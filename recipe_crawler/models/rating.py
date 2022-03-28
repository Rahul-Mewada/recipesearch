
class Rating:
    def __init__(self, rating_dict):
        if rating_dict.get('@type') == 'AggregateRating':
            for key in rating_dict:
                value = rating_dict.get(key)
                match key:
                    case 'ratingCount':
                        self.count = value
                    case 'ratingValue':
                        self.value = value

    def __str__(self):
        return f"Rating value: {self.count}\nRating count: {self.value}"
    
    def __repr__(self) -> str:
        return f"Rating value: {self.count}\nRating count: {self.value}"

    def to_json(self):
        return dict(
            count = self.count,
            value = self.value
        )