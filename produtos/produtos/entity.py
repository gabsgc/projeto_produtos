class Produto():
    def __init__(self, id:int, name: str, description: str, price: float, image: str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image
""" 
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self.name = value

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, value):
        self.description = value

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        self.price = value

    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, value):
        self.image = value """