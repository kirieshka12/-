#задание 1
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        if not isinstance(new_password, str):
            raise ValueError("Пароль должен быть строкой.")
        if len(new_password) < 6:
            raise ValueError("Пароль слишком короткий. Минимум 6 символов.")
        self.__password = new_password
        print("Пароль успешно изменён.")

    def check_password(self, password):
        return password == self.__password


user = UserAccount("123", "123@example.com", "secret123")
print(user.username, user.email)

print("Правильный пароль?", user.check_password("secret123"))  # True
print("Неправильный пароль?", user.check_password("wrong"))    # False


user.set_password("newpass456")
print("Проверка нового пароля:", user.check_password("newpass456"))  # True

#задание 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make   # марка
        self.model = model # модель

    def get_info(self):
        return f"Транспорт: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type   

    def get_info(self):
        return f"Автомобиль: {self.make} {self.model}, Топливо: {self.fuel_type}"

v = Vehicle("BMW", "X5 G05")
print(v.get_info()) 

c = Car("BMW", "X5 G05", "бензин")
print(c.get_info()) 
vehicles = [v, c]
for item in vehicles:
    print(item.get_info())