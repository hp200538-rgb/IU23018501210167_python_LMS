#library-management-system,insert bookname,upadte bookname,delete bookname,view bookname,search bookname
class Book:
    def __init__(self, bid,b_authorname, title):  
        self.bid = bid
        self.b_authorname = b_authorname
        self.title = title
    def display(self):
        print(f"Book ID: {self.bid},  Author Name: {self.b_authorname}, Title: {self.title}")     
class Library:
    def __init__(self):
        self.book = []
    def insert_book(self, book):       #insert book
        self.book.append(book)
        print("Book is inserted")
    def update_book(self,bid,new_name):   #update book
        for book in self.book:
            if book.bid == bid:
                book.title=new_name
                print("book name is updated")
                return
        print("Book not found")
    def delete_book(self,bid):      #delete book
        for book in self.book:
            if book.bid == bid:
                self.book.remove(book)
                print("Book is delete")
                return
        print("Book not found")
    def view_books(self):                               #view book
        if not self.book:
            print("No books available")
            return
        for book in self.book:
            book.display()
    def search_book(self,bid):                      #search book
        for book in self.book:
            if book.bid == bid:
                book.display()
                return
        print("Book not found")
lib = Library()
while True:
    print("\nLibrary Management System")
    print("1. Insert Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. View Books")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        bid = input("Enter Book ID: ")
        b_authorname = input("Enter Author Name: ")
        title = input("Enter Book Title: ")
        book = Book(bid,b_authorname, title)
        lib.insert_book(book)
    elif choice == '2':
        bid = input("Enter Book ID to update: ")
        new_name = input("Enter new Book Title: ")
        lib.update_book(bid,new_name)
    elif choice == '3':
        bid = input("Enter Book ID to delete: ")
        lib.delete_book(bid)
    elif choice == '4':
        lib.view_books()
    elif choice == '5':
        bid = input("Enter Book ID to search: ")
        lib.search_book(bid)
    elif choice == '6':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")