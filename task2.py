BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book

class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'

# TODO написать класс Library

class Library:
    def __init__(self, books=None):
        # Если список книг не передан, инициализируем пустой список
        self.books = books if books is not None else []

    def get_next_book_id(self):
        # Если в библиотеке нет книг, возвращаем 1
        if not self.books:
            return 1
        # Если книги есть, возвращаем id следующей книги
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        # Ищем книгу с указанным id
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        # Если книга не найдена, возбуждаем ошибку
        raise ValueError(f"Книги с запрашиваемым id {book_id} не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
