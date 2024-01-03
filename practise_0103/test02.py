class Library :   

    class Books :
        def __init__(self,id,bookname,year,writer) :
            self.bookname = bookname
            self.id = id 
            self.year = year
            self.writer = writer


    class User:
        def __init__(self,name,id):
            self.Username = name 
            self.Userid = id 
            self.books = {}
            
        def add_book(self, book) : 
            if book.id not in self.books:
                self.books[book.id] = book
                print(f"{self.Username} 借閱 : {book.bookname} ID : {book.id} 年份 : {book.year} 作者 : {book.writer}")
            else :
                print(f"{book.bookname} 已經被借出")

        def reture_book(self, book) :
            if book.id in self.books:
                returned_book = self.books[book.id]
                del self.books[book.id]
                print(f"{self.Username} 還書 : {returned_book.bookname} ID : {book.id} 年份 : {returned_book.year} 作者 : {returned_book.writer}")
            else :
                print(f"{book.id} 並沒有借這本書")

        def Inquire_books(self) : 
            if not self.books:
                print(f"{self.Username} 沒有借任何書 ")
            else :
                print(f"{self.Username} 目前借閱的書 :")
                for book_id , book in self.books.items() : 
                    print(f"書籍 ID ： {book_id}, 書名：{book.bookname} 作者：{book.writer} 年份：{book.year}")

#ex
library = Library()

book1 = library.Books("001","A1","2024","andy")
book2 = library.Books("002","S2","2022","mike")

user1 = library.User("Jhon","022")

user1.add_book(book1)
user1.add_book(book2)
user1.Inquire_books()

user1.reture_book(book2)
user1.Inquire_books()
