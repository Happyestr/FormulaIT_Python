# TODO Написать 3 класса с документацией и аннотацией типов
class Employee:
    def __init__(self, name: str, salary: int):
        """
        Создание и подготовка к работе объекта "Рабочий"
        :param name: Имя
        :param salary: Зарплата
        Примеры:
        >>> employee = Employee("name", 50000)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError
        self.name = name
        if not isinstance(salary, (int, float)):
            raise TypeError
        if salary <= 0:
            raise ValueError
        self.salary = salary

    def print_name(self):
        """
        Функция печатает имя Рабочего
        Примеры:
        >>> employee = Employee("name", 50000)
        >>> employee.print_name()
        """
        ...


    def print_salary(self):
        """
        Функция печатает зарплату Рабочего
        Примеры:
        >>> employee = Employee("name", 50000)
        >>> employee.print_salary()
        """
        ...

    def print_employee(self):
        """
        Функция печатает все поля Рабочего
        Примеры:
        >>> employee = Employee("name", 50000)
        >>> employee.print_employee()
        """
        ...


class Window:
    def __init__(self, height: float, width: float, position: bool):
        """
        Cоздание и подготовка к работе объекта "Окно"
        :param height: Высота окна
        :param age: Возраст окна
        :param position: Позиция окна (true - открыто, false - закрыто)
        Примеры:
        >>> window = Window(90, 50, True)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError
        if height <= 0:
            raise ValueError
        self.height = height
        if not isinstance(width, (int, float)):
            raise TypeError
        if width < 0:
            raise ValueError
        self.width = width
        if not isinstance(position, bool):
            raise TypeError
        self.position = position

    def open_window(self) -> None:
        """
        Функция открывает окно
        :raise ValueError: Если окно уже открыто
        Примеры:
        >>> window = Window(90, 50, False)
        >>> window.open_window()
        """
        ...

    def close_window(self) -> None:
        """
        Функция закрывает окно
        :raise ValueError: Если окно уже закрыто
        Примеры:
        >>> window = Window(90, 50, True)
        >>> window.close_window()
        """
        ...

MAX_WIDTH = 1000
MAX_HEIGHT = 1000

class Button:
    def __init__(self, x: int, y: int, name: str):
        """
        Cоздание и подготовка к работе объекта "Кнопка"
        :param x: Координата кнопки по x
        :param y: Координата кнопки по y
        :param name: Надпись на кнопке
        Примеры:
        >>> button = Button(300, 500, "Кнопка")  # инициализация экземпляра класса
        """
        if not isinstance(x, int):
            raise TypeError
        if x < 0 or x > MAX_WIDTH: #MAX_WIDTH - ширина экрана
            raise ValueError
        self.x = x
        if not isinstance(y, int):
            raise TypeError
        if y < 0 or y > MAX_HEIGHT: #MAX_HEIGHT - высота экрана
            raise ValueError
        self.y = y
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def move(self, x: int, y: int) -> None:
        """
        Функция перемещает кнопку на новые координаты
        :raise ValueError: Если значения некорректны(Проверка такая же как в __init__)
        Примеры:
        >>> button = Button(300, 500, "Кнопка")
        >>> button.move(100, 200)
        """
        if not isinstance(x, int):
            raise TypeError
        if x < 0 or x > MAX_WIDTH: #MAX_WIDTH - ширина экрана
            raise ValueError
        self.x = x
        if not isinstance(y, int):
            raise TypeError
        if y < 0 or y > MAX_HEIGHT: #MAX_HEIGHT - высота экрана
            raise ValueError
        self.y = y
        ...

    def new_name(self, new_name: str) -> None:
        """
        Функция ставит кнопки новое название
        :raise TypeError: Если не str
        Примеры:
        >>> button = Button(300, 500, "Кнопка")
        >>> button.new_name("Новая кнопка")
        """
        if not isinstance(new_name, str):
            raise TypeError
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
