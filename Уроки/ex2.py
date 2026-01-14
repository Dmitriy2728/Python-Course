from book import Book

Library =[
    Book("Черновик", "С.Лукьяненко"),
    Book("War", "S.Tarmashev"),
    Book("Corporation", "S.Tarmashev")
]

for Book in Library:
    print(f"{Book.name} - {Book.writer}") 
    
