#library management System

class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showInfo(self):
        print(f"The Library has {self.noBooks} books and the name of books is {self.books}")

L1=Library()
L1.addBook("Harry potter")
L1.addBook("Tom and Jerry")
L1.showInfo()