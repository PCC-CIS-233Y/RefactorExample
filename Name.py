from dataclasses import dataclass

@dataclass
class Name:
    __text: str = ""
    __year: int = 0
    __gender: str = ""
    __count: int = 0

    #Constructor
    def __init__(self, text, year, gender, count):
        self.__text = text
        self.__year = year
        self.__gender = gender
        self.__count = count

    @property
    def text(self):
        return self.__text

    @property
    def year(self):
        return self.__year

    @property
    def gender(self):
        return self.__gender

    @property
    def count(self):
        return self.__count

    @staticmethod
    def readNames(year, gender):
        from Database import Database

        return Database.readNames(year, gender)