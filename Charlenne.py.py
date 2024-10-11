class Library:
    def __init__(self):
        self.available_books = []
        self.reservation_queue = [] 
        self.undo_stack = [] 
    def add_book(self, book):
        self.available_books.append(book)
    def reserve_book(self, user_id, book):
        if book in self.available_books:
            self.available_books.remove(book)
            self.undo_stack.append((user_id, book))
            print(f"Book '{book}' reserved for user '{user_id}'.")
        else:
            self.reservation_queue.append((user_id, book))
            print(f"Book '{book}' not available. Added to queue for user '{user_id}'.")
    def undo_reservation(self):
        if self.undo_stack:
            user_id, book = self.undo_stack.pop()
            self.available_books.append(book)  
            print(f"Reservation for book '{book}' by user '{user_id}' has been undone.")
        else:
            print("No reservations to undo.")
    def process_queue(self):
        while self.reservation_queue:
            user_id, book = self.reservation_queue.pop(0) 
            if book in self.available_books:
                self.available_books.remove(book)
                self.undo_stack.append((user_id, book))
                print(f"Book '{book}' reserved for user '{user_id}' from queue.")
                break 
    
library = Library()
library.add_book("Book A")
library.add_book("Book B")

library.reserve_book("User1", "Book A")
library.reserve_book("User2", "Book B")
library.reserve_book("User3", "Book C") 
library.undo_reservation() 
library.process_queue()  
