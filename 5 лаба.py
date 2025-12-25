# 1 задание
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


my_book = Book("Мастер и Маргарита", "м. Булгаков", 1967)
print(my_book.get_info())

# 2 задание
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

c = Circle(5)
print("Начальный радиус:", c.get_radius())

c.set_radius(10)
print("Новый радиус:", c.get_radius())