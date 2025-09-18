from movie_lib import *


def main():
    menu = input("""
        Enter 1 add name
        Enter 2 rate movie
        Enter 3 view average rating
        Enter 4 exit     
             """)
    name = MovieLib()
    match menu:
        case "1":
            movie_producer = input("Enter the movie producer:\n")
            movie_name = input("Enter the movie name:\n")
            name.create_movie(movie_producer,movie_name)
            print("movie name is added successfully...")
            main()

        case "2":
            movie_producer = input("Enter the movie producer:\n")
            ratings = int(input("Enter your rating count:\n"))
            print(movie_rating(movie_producer,ratings))
            main()

        case "3":
            movie_producer = input("Enter the movie producer name:\n")
            print(calculate_average_rating(movie_producer))
            main()






main()
