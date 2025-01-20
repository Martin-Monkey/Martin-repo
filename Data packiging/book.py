import json
import pickle

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"


    def to_json(self):
        return json.dumps(self.__dict__)


    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(**data)


    def to_pickle(self):
        return pickle.dumps(self)


    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)
