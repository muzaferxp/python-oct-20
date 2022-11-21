import data

def crateBook(bookContent):
    data.books.append(bookContent)
    print("=========ADDED NEW BOOK==========")
    
def updateBook(id, updateContent): 
    for book in data.books:
        if book['id'] == id:
            index = data.books.index(book)
            data.books[index] = updateContent
    
    print("=========UPDATED BOOK==========")
   
def deleteBook(id):
    temp = []
    for item in data.books:
        if item['id'] != id:
            temp.append(item)
            
    data.books = temp

# to get a single book details by id
def getBookById(id):
    for item in data.books:
        if id == item['id']:
            print(item)
            break

def getAllBooks():
    print(data.books)

def rentBook(id, status):
    for book in data.books:
        if book['id'] == id:
            index = data.books.index(book)
            data.books[index] = status
    
    print("=========UPDATED BOOK==========")
   