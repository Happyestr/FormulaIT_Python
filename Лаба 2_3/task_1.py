class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self): #Только геттеры, потому что атрибуты изменяться не могут по заданию
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self): # Этот метод можно использовать для всех классов
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self): # Этот метод нужно переписать для дочерних классов т.к не учитывает pages или duration
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author) # Можно использовать метод базового класса для определения author и name
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author) # Можно использовать метод базового класса для определения author и name
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if duration < 0:
            raise ValueError
        self._duration = duration


    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

book = Book('1', 'author1')
paper = PaperBook('2', 'author2', 500)
audio = AudioBook('3', 'author3', 100.1)
print("Метод repr:", book.__repr__(), "Метод srt:", book.__str__())
print("Метод repr:", paper.__repr__(), "Метод srt:", paper.__str__())
print("Метод repr:", audio.__repr__(), "Метод srt:", audio.__str__())

