from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"Leaf: {self.name}"


class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        """Method to add elements to the Composite."""
        self.children.append(component)

    def remove(self, component):
        """Method to remove elements from the Composite."""
        self.children.remove(component)

    def operation(self):
        results = [f"Composite: {self.name}"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)


if __name__ == "__main__":
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")
    leaf3 = Leaf("Leaf 3")

    composite1 = Composite("Composite 1")
    composite2 = Composite("Composite 2")

    # Adding Leaf elements to Composite 1
    composite1.add(leaf1)
    composite1.add(leaf2)

    # Adding Composite 1 and Leaf 3 to Composite 2
    composite2.add(composite1)
    composite2.add(leaf3)

    # Displaying the structure and executing operations
    print(composite2.operation())
