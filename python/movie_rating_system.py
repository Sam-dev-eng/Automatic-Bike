import datetime

class Movie:
    def __init__(self):
        self._name = None
        self._producer = None
        self._raters = []
        self._average_rating = None

        self.date = datetime.datetime.now().replace(microsecond=0)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self , value):
        self._name = value

    @property
    def average_ratings(self):
        return self._average_rating

    @average_ratings.setter
    def average_ratings(self, value):
        self._average_rating = value


    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, number):
        self._producer = number

    def get_date(self):
        return self.date

    def __str__(self):
        return f"{self._producer} by {self.name}"
    @property
    def raters(self):
        return self._raters

    @raters.setter
    def raters(self, value):
        self._raters.append(value)




