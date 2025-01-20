import json
import pickle
from book import Book

# Create a Book instance
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)


book_json = book1.to_json()
print("Serialized to JSON:")
print(book_json)


book_from_json = Book.from_json(book_json)
print("\nDeserialized from JSON:")
print(book_from_json)


book_pickle = book1.to_pickle()
print("\nSerialized to Pickle:")
print(book_pickle)


book_from_pickle = Book.from_pickle(book_pickle)
print("\nDeserialized from Pickle:")
print(book_from_pickle)
