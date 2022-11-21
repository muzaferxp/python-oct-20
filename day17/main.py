import librarySystem

book = {
    "id" : 4,
    "name" : "Book 4",
    "isAvailable" : True
}

librarySystem.crateBook(book)

librarySystem.updateBook(2, {
    "id" : 2,
    "name" : "Update name 2",
    "isAvailable" : False
})

librarySystem.getBookById(2)

librarySystem.deleteBook(3)


librarySystem.rentBook(2, {
    "id" : 2,
    "name" : "Update name 2",
    "isAvailable" : False
})

librarySystem.getAllBooks()