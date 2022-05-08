class Book:
    author: str
    title: str
    price: float
    book_id: int

    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    # define the necessary method here
    def __str__(self):
        return "{} by {}. ${}. [{}]".format(self.title, self.author, round(self.price, 2), self.book_id)

