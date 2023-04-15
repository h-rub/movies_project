class Movie:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

    def save_movie(self):
        print(f"Guardando la pelicula '{self.title}'")

    def __str__(self):
        return f"{self.title} - {self.year} - {self.score}"