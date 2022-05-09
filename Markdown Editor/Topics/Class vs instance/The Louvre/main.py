class Painting:

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return '"{}" by {} ({}) hangs in the Louvre.'.format(self.title, self.artist, self.year)


painting_1 = Painting(input(), input(), input())
print(painting_1)
