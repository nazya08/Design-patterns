import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Person(Prototype):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}, Address: {self.address}"


class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def __str__(self):
        return f"{self.street}, {self.city}"


class Car(Prototype):
    def __init__(self, make, model, owner):
        self.make = make
        self.model = model
        self.owner = owner

    def __str__(self):
        return f"Car: {self.make} {self.model}, Owner: {self.owner}"


if __name__ == "__main__":
    # Створення оригінальних об'єктів
    original_person = Person("John Doe", 30, Address("123 Elm St", "Springfield"))
    original_car = Car("Tesla", "Plaid", original_person)

    # Клонування об'єктів
    cloned_person = original_person.clone()
    cloned_car = original_car.clone()

    cloned_person.name, cloned_person.age = "Nazar Filoniuk", 19
    cloned_person.address.street = "255 Elm St"
    cloned_car.make, cloned_car.model = "BMW", "M5 E34"

    print("Original Person:\n", original_person)
    print("Cloned Person:\n", cloned_person)
    print("\nOriginal Car:\n", original_car)
    print("Cloned Car:\n", cloned_car)
