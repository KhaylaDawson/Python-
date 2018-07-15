class Movie(object):

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __str__(self):
        return self.title + " has a rating of " + str(self.rating)

class Action(Movie):
    def content(self):
        return "Bang!"

class Comedy(Movie):
    def content(self):
        return "Haha!"

class Drama(Movie):
    def content(self):
        return "I can't believe you"

movies = [Action("Die Hard", 10), Comedy("Austin Powers", 8), Drama("Crash", 9)]
for movie in movies:
    print(movie, movie.content())

    
