import unittest

from movie_rating_system import Movie


class MyTestCase(unittest.TestCase):
    def test_the_current_name_of_the_movie(self):
        movie = Movie()
        self.assertEqual(movie.name, None)

    def test_when_the_name_is_changed(self):
        movie = Movie()
        movie.name = "The red devils"
        self.assertEqual(movie.name, "The red devils")

    def test_the_default_rating(self):
        movie = Movie()
        self.assertEqual(movie.producer, None)

    def test_When_the_rating_is_changed(self):
        movie = Movie()
        movie.producer = "Sam"
        self.assertEqual(movie._producer, "Sam")




if __name__ == '__main__':
    unittest.main()

