from movie_rating_system import Movie


movie_lib = []
class MovieLib:
        def __init__(self):
            self.movie_data = []
            self.movie = Movie()

        def create_movie(self,movie_name,movie_producer):
            self.movie.name = movie_name
            self.movie.producer = movie_producer
            self.movie_data.append(self.movie)
            movie_lib.append(self.movie_data)


        def set_average_ratings(self,value):
            self.movie.average_ratings = calculate_average_rating(value)


def movie_rating(name_of_movie, number_of_rate):
    for items in movie_lib:
        for movies in items:
            if movies.name == name_of_movie:
                movies.raters = number_of_rate
                return "Thanks for rating " + movies.name
    return "This movie does not exist in this library"

def movie_average(name_of_movie):
    for items in movie_lib:
        for movies in items:
            if movies.name == name_of_movie:
                return movies.average_ratings
    return "This movie does not exist in this library"

def calculate_average_rating(name_of_movie):
    for items in movie_lib:
        for movies in items:
            if movies.name  == name_of_movie:
                total_sum = 0
                for number in movies.raters:
                    total_sum += number
                average_rating = total_sum / len(movies.raters)
                rounded = round(average_rating, 2)
                return rounded
    return "This movie does not exist in this library"

def rating_count(name):
    for items in movie_lib:
        for movies in items:
            if movies.name  == name:
                return movies.raters
    return []



# mov = MovieLib()
# mov.create_movie("sam","Things fall Apart")
# print(movie_rating("sam", 22))
# print(movie_rating("sam", 24))
# print(movie_rating("sam", 40))
# print(rating_count("sam"))
# print(calculate_average_rating("sam"))


