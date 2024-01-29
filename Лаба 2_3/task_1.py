class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name # для name и author были добавлены подчеркивания, чтобы сделать эти переменные защищенными
        self._author = author

    def __str__(self): # Этот метод можно использовать для всех классов
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self): # Этот метод нужно переписать для дочерних классов т.к не учитывает pages или duration
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author) # Можно использовать метод базового класса для определения author и name
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author) # Можно использовать метод базового класса для определения author и name
        if not isinstance(duration, float):
            raise TypeError
        if duration < 0:
            raise ValueError
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

book = Book('1', 'author1')
paper = PaperBook('2', 'author2', 500)
audio = AudioBook('3', 'author3', 100.1)
print("Метод repr:", book.__repr__(), "Метод srt:", book.__str__())
print("Метод repr:", paper.__repr__(), "Метод srt:", paper.__str__())
print("Метод repr:", audio.__repr__(), "Метод srt:", audio.__str__())