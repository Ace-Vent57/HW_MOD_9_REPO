

import unittest
from booklover import BookLover  # lowercase 'booklover'


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        bl = BookLover("Test User", "test@example.com", "fiction")
        bl.add_book("Harry Potter", 5)
        self.assertTrue("Harry Potter" in bl.book_list['book_name'].values)
    
    def test_2_add_book(self):
        bl = BookLover("Test User", "test@example.com", "fiction")
        bl.add_book("Harry Potter", 5)
        bl.add_book("Harry Potter", 4)  # Attempt to add again
        self.assertEqual(bl.book_list['book_name'].value_counts().get("Harry Potter", 0), 1)
    
    def test_3_has_read(self):
        bl = BookLover("Test User", "test@example.com", "fiction")
        bl.add_book("Moby Dick", 4)
        self.assertTrue(bl.has_read("Moby Dick"))
    
    def test_4_has_read(self):
        bl = BookLover("Test User", "test@example.com", "fiction")
        self.assertFalse(bl.has_read("Nonexistent Book"))
    
    def test_5_num_books_read(self):
        bl = BookLover("Test User", "test@example.com", "fiction")
        bl.add_book("Book 1", 3)
        bl.add_book("Book 2", 4)
        bl.add_book("Book 3", 5)
        self.assertEqual(bl.num_books_read(), 3)
    
    def test_6_fav_books(self):
        bl = BookLover("Test User", "test@example.com", "fiction")
        bl.add_book("Book 1", 3)
        bl.add_book("Book 2", 4)
        bl.add_book("Book 3", 5)
    
    # fav_books = bl.fav_books()  # This is a NumPy array of book names

    # # Check that all returned book names are in the expected list
    # expected_books = ["Book 2", "Book 3"]
    # self.assertTrue(set(fav_books) == set(expected_books))

if __name__ == '__main__':
    unittest.main()
