

# Create a class called BookLover

# The class should have the following attributes
# - name (str): The name of the book lover
# - email (str): The email of the book lover
# - fav_genre (str): The favorite genre of the book lover
# - num_books (int): The number of books the book lover has read
# - book_list (DataFrame): A DataFrame with the columns 'book_name' and 'book_rating' that stores the books the book lover has read




# The class should have the following methods
# - add_book: A method that takes a book name and a book rating and adds it to the book_list. If the book is already in the book_list print a message saying that the book is already in the list. If the book is not in the list, add it to the book_list and increment the num_books attribute by 1. The method should print a message saying that the book has been added.
# - has_read: A method that takes a book name and returns True if the book is in the book_list and False otherwise.
# - num_books_read: A method that returns the num_books attribute.
# - fav_books: A method that returns a list of the book names of the books in the book_list with a rating of more than 3.


import pandas as pd

class BookLover:
      def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})
      
      def add_book(self, book_name, book_rating):
            # check if the book is already in the book_list
            if book_name in self.book_list['book_name'].values:
                print(f'{book_name} is already in the list')
            else:
                # Create a new book entry
                new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
                self.num_books += 1

                print(f'{book_name} has been added')
            
      def has_read(self, book_name):
          return book_name in self.book_list['book_name'].values

      def num_books_read(self):
          return self.num_books

      def fav_books(self):
          return self.book_list[self.book_list['book_rating'] > 3]['book_name'].values 


# Testing the class
if __name__ == '__main__':
    test_object = BookLover("Chuck Barry", "hsolo@millenniumfalcon.com", "Rock n roll scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Dune", 5)
    test_object.add_book("Space Balls", 3)  # Duplicate entry test
    print("Has read 'Dune'?", test_object.has_read("Dune"))
    print("Number of books read:", test_object.num_books_read())
    print("Favorite books:")
    print(test_object.fav_books())
