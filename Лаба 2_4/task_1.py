class Automibile:
    """
    Класс "Автомобиль". Базовый класс
    :param mark: Марка машины (неименяемая переменная)
    :param wheels: Количество колес (неименяемая переменная)
    :param color: Цвет машины (защищенная переменная с сеттером, т.к можно изменить цвет)
    :param fuel: Топливо в машине
    """
    def __init__(self, mark: str, wheels: int, color: str, fuel: float) -> None:
        self._mark = mark
        self._wheels = wheels
        self._color = color
        self.set_fuel(fuel)

    @property
    def mark(self) -> str:  # Только геттеры, потому что атрибуты изменяться не могут
        return self._mark

    @property
    def wheels(self) -> int:
        return self._wheels

    @property
    def color(self) -> str:
        return self._color

    @color.setter  # Можно установить новый цвет автомобиля, если перекрасили
    def color(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError
        self._color = color

    def set_fuel(self, fuel: float):
        """
        Метод устанавливает значение fuel
        """
        if not isinstance(fuel, float):
            raise TypeError
        if fuel <= 0:
            raise ValueError
        self.fuel = fuel

    def print_fuel(self) -> str:
        """Возвращает количество топлива"""
        return f"Количество топлива:{self.fuel}."

    def print_kilometrage(self) -> str:
        """
        Возвращает оставшееся расстояние, которое можно проехать без дозаправки.
        Рассчет идет исходя из среднего расхода топлива
        """
        return f"Осталось топлива на:{(self.fuel/16) * 100}"

    def add_fuel(self, fuel_to_add: float) -> None:
        """
        Метод, который позволяет добавить топливо в переменную fuel, если, например, долили
        """
        if not isinstance(fuel_to_add, float):
            raise TypeError
        if fuel_to_add <= 0:
            raise ValueError
        self.fuel += fuel_to_add

    def __str__(self) -> str:
        return f"Машина марки:{self._mark}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mark={self._mark!r}, wheels={self._wheels}, color={self._color}, fuel={self.fuel})"


class PassengerCar(Automibile):
    """
    Класс "Легковой автомобиль". Дочерний класс класса "Автомобиль"
    :param mark: Марка машины (неименяемая переменная)
    :param wheels: Количество колес (неименяемая переменная)
    :param color: Цвет машины (защищенная переменная с сеттером, т.к можно изменить цвет)
    :param fuel: Топливо в машине
    :param seats: Количество сидений в машине (неименяемая переменная)
    :param empty_seats: Свободное количество мест
    """
    def __init__(self, mark: str, wheels: int, color: str, fuel: float, seats: int, empty_seats: int) -> None:
        super().__init__(mark, wheels, color, fuel)
        self._seats = seats  # Общее количество мест. Изменяться не может
        self.set_seats(empty_seats)  # Количество свободных мест

    @property
    def seats(self) -> int:
        return self._seats

    def set_seats(self,
                               new_seats: int) -> None:  # Изменить количество свободных мест (например, если в машину сели люди)
        """Функция изменяет количество свободных мест, если, например, кто то сел в машину"""
        if not isinstance(new_seats, int):
            raise TypeError
        if new_seats < 0:
            raise ValueError
        self.empty_seats = new_seats

    def print_kilometrage(self) -> str:
        """Перегружаем функцию базового класса, т.к расход топлива у легковой машины меньше чем средний статистический"""
        return f"Осталось топлива на:{(self.fuel/10) * 100}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mark={self._mark!r}, wheels={self._wheels}, color={self._color}, fuel={self.fuel}, seats={self._seats}, empty seats={self.empty_seats})"


class Cargo(Automibile):
    """
    Класс "Грузовой автомобиль". Дочерний класс класса "Автомобиль"
    :param mark: Марка машины (неименяемая переменная)
    :param wheels: Количество колес (неименяемая переменная)
    :param color: Цвет машины (защищенная переменная с сеттером, т.к можно изменить цвет)
    :param fuel: Топливо в машине
    :param capacity: Вместимость грузового автомобиля (неименяемая переменная)
    :param remaining_capacity: Оставшееся свободное место
    """
    def __init__(self, mark: str, wheels: int, color: str, fuel: float, capacity: int, remaining_capacity: int) -> None:
        super().__init__(mark, wheels, color, fuel)
        self._capacity = capacity #Вместимость грузовой машины. Неизменяемая переменная
        self.remaining_capacity = remaining_capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    def set_capacity(self, capacity: int) -> None: #Изменить оставшуюся грузоподьемность (например, если что-то положили)
        """Изменяет свободное место в грузовом автомобиле, например, если что-то положили."""
        if not isinstance(capacity, int):
            raise TypeError
        if capacity < 0:
            raise ValueError
        self.remaining_capacity = capacity

    def print_kilometrage(self) -> str:
        """Перегружаем функцию базового класса, т.к расход топлива у грузовой машины больше чем средний статистический"""
        return f"Осталось топлива на:{(self.fuel/30) * 100}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mark={self._mark!r}, wheels={self._wheels}, color={self._color}, fuel={self.fuel}, seats={self._capacity}, empty seats={self.remaining_capacity})"


if __name__ == "__main__":
    # Write your solution here
    pass