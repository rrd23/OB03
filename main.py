import json


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def make_sound(self):
        pass

    def eat(self):
        return f"{self.name} is eating."

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} chirps."

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} roars."

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} hisses."

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Employee():
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        return f"{self.name} feeds {animal.name}."

class Veterinarian(Employee):
    def heal_animal(self, animal):
        return f"{self.name} heals {animal.name}."

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            "animals": [{"name": a.name, "age": a.age, "type": type(a).__name__} for a in self.animals],
            "employees": [{"name": e.name, "type": type(e).__name__} for e in self.employees]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load_from_file(cls, filename):
        zoo = cls()
        with open(filename, 'r') as f:
            data = json.load(f)
        for animal_data in data["animals"]:
            animal_class = globals()[animal_data["type"]]
            zoo.add_animal(animal_class(animal_data["name"], animal_data["age"]))
        for employee_data in data["employees"]:
            employee_class = globals()[employee_data["type"]]
            zoo.add_employee(employee_class(employee_data["name"]))
        return zoo

# Пример использования
zoo = Zoo()

# Добавление животных
zoo.add_animal(Bird("Tweety", 2))
zoo.add_animal(Mammal("Leo", 5))
zoo.add_animal(Reptile("Snakey", 3))

# Добавление сотрудников
zoo.add_employee(ZooKeeper("John"))
zoo.add_employee(Veterinarian("Alice"))

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Сохранение состояния зоопарка
zoo.save_to_file("zoo_state.json")

# Загрузка состояния зоопарка
loaded_zoo = Zoo.load_from_file("zoo_state.json")

# Проверка загруженных данных
print("\nЗагруженные животные:")
for animal in loaded_zoo.animals:
    print(f"{animal.name} ({type(animal).__name__})")

print("\nЗагруженные сотрудники:")
for employee in loaded_zoo.employees:
    print(f"{employee.name} ({type(employee).__name__})")