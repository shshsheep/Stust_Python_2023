class library :
    def __init__(self,id,year,writer,where) :
        self.id = id 
        self.year = year
        self.writer = writer 
        self.books = {}
        self.where = where
        # self.time = ''

    def add_book(self, book, time) : 
        if book not in self.books:
            self.books[book] = time
            print(f"借閱 : {book} ID : {self.id} 年份 : {self.year} 作者 : {self.writer} 借出時間 : {time}")
        else :
            print(f"{book} 已經被借出")
    def reture_book(self, book) :
        if book in self.books:
            del self.books[book]
            print(f"還書 : {book} ID : {self.id} 年份 : {self.year} 作者 : {self.writer}")
        else :
            print(f"{book} 並沒有借這本書")
    def Inquire(self, book) : 
        if book in self.books:
            print(f"{book} 已借出 借出時間 : {self.books[book]} ")
        else :
            print(f"{book} 這本書還未被借出  書在 : {self.where}")

#ex
library_books = library("001","2022","andy","2F-1")

library_books.add_book("A1","2024-01-03")
library_books.add_book("S2","2024-01-01")
library_books.add_book("B3","2024-01-01")
print(library_books.books)

library_books.reture_book("S2")

library_books.Inquire("A1")
library_books.Inquire("S2")
library_books.Inquire("B3")
print(library_books.books)
