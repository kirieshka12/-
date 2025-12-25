# Базовый класс сотрудника
class Employee:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def get_info(self) -> str:
        return f"Сотрудник: {self.name}, ID: {self.id}"


# Класс менеджера с дополнительным атрибутом department и методом управления проектом
class Manager(Employee):
    def __init__(self, name: str, id: int, department: str):
        super().__init__(name, id)
        self.department = department

    def manage_project(self, project_name: str) -> str:
        return f"{self.name} (Менеджер отдела {self.department}) управляет проектом '{project_name}'."

    def get_info(self) -> str:
        return f"Менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}"


# Класс техника с атрибутом specialization и методом выполнения обслуживания
class Technician(Employee):
    def __init__(self, name: str, id: int, specialization: str):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self, equipment: str) -> str:
        return f"{self.name} (Техник, специализация: {self.specialization}) выполняет обслуживание оборудования: {equipment}."

    def get_info(self) -> str:
        return f"Техник: {self.name}, ID: {self.id}, Специализация: {self.specialization}"


# Класс, сочетающий Manager и Technician
class TechManager(Manager, Technician):
    def __init__(self, name: str, id: int, department: str, specialization: str):
        # Для простоты явно вызываем конструктор базового класса Employee
        Employee.__init__(self, name, id)
        self.department = department
        self.specialization = specialization
        # Список подчинённых
        self.team = []

    # Переопределяем методы для более удобных сообщений
    def manage_project(self, project_name: str) -> str:
        return f"{self.name} (TechManager, отдел: {self.department}) управляет проектом '{project_name}'."

    def perform_maintenance(self, equipment: str) -> str:
        return f"{self.name} (TechManager, специализация: {self.specialization}) выполняет обслуживание: {equipment}."

    def add_employee(self, employee: Employee) -> None:
        """Добавить сотрудника в список подчинённых."""
        self.team.append(employee)

    def get_team_info(self) -> str:
        """Вернуть информацию о всех подчинённых."""
        if not self.team:
            return f"У {self.name} нет подчинённых."
        info_lines = [f"Команда {self.name}:"]
        for emp in self.team:
            info_lines.append(" - " + emp.get_info())
        return "\n".join(info_lines)

    def get_info(self) -> str:
        return f"TechManager: {self.name}, ID: {self.id}, Отдел: {self.department}, Специализация: {self.specialization}"


# Демонстрация функциональности
if __name__ == "__main__":
    # Создаём обычного сотрудника
    emp = Employee("Иван Петров", 101)
    print(emp.get_info())

    # Создаём менеджера
    mgr = Manager("Ольга Сидорова", 102, "R&D")
    print(mgr.get_info())
    print(mgr.manage_project("Альфа"))

    # Создаём техника
    tech = Technician("Сергей Иванов", 103, "Сетевые устройства")
    print(tech.get_info())
    print(tech.perform_maintenance("Роутер X200"))

    # Создаём TechManager
    tech_mgr = TechManager("Анна Козлова", 200, "Продукт", "Встроенные системы")
    print(tech_mgr.get_info())
    print(tech_mgr.manage_project("Бета"))
    print(tech_mgr.perform_maintenance("Датчик A1"))

    # Добавляем подчинённых
    tech_mgr.add_employee(emp)
    tech_mgr.add_employee(mgr)
    tech_mgr.add_employee(tech)

    # Выводим информацию о команде
    print(tech_mgr.get_team_info())