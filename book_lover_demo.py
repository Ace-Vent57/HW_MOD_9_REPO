

from booklover.booklover import BookLover

# Create a BookLover object
book_lover = BookLover("ACE", "xyz@gmail.com", "Science Fiction")
 
# Add a book
book_lover.add_book("Dune", 5)
 
# Print number of books read
print("Number of books read:", book_lover.num_books_read())