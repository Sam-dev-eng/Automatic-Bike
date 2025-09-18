


class Human:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
       return self._name


    @name.setter
    def name(self, value):
        self._name = value

sam = Human("Sam")
sam.name = "Maka"
print(sam.name)