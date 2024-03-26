class Restaurant:
    # Constructor
    def __init__(self, name: str, cuisine: str, pricing: str, rating: float, address: str):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.pricing = pricing
        self.address = address
    # Accessors
    def get_name(self) -> str: return self.name
    def get_cuisine(self) -> str: return self.cuisine 
    def get_rating(self) -> str: return self.rating
    def get_pricing(self) -> str: return self.pricing
    def get_address(self) -> str: return self.address
    # String representation
    def __str__(self) -> str:
        dashed_line = '-' * 40
        return "{0}\n\nName: {1}\nCuisine: {2}\nRating: {3}/5\nPricing: {4}/5\nAddress: {5}\n\n{0}".format(dashed_line, self.name, self.cuisine, self.rating, self.pricing, self.address)