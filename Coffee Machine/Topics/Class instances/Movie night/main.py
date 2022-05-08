class Movie:
    # create class here
    title: str
    director: str
    year: int

    def __init__(self, title: str, director: str, year: int):
        self.title = title
        self.director = director
        self.year = year


# objects of the class Movie
year_titanic: int = 1997
year_star_wars: int = 1977
year_fight_club: int = 1999
titanic = Movie("Titanic", "James Cameron", year_titanic)
star_wars = Movie("Star Wars", "George Lucas", year_star_wars)
fight_club = Movie("Fight Club", "David Fincher", year_fight_club)
