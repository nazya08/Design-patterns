from abc import ABC, abstractmethod
from random import randint
from typing import List


class Publisher(ABC):

    @abstractmethod
    def add_subscriber(self, subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber):
        pass

    @abstractmethod
    def notify_subscriber(self):
        pass


class ConcretePublisher(Publisher):
    def __init__(self):
        self.state = None
        self.subscribers: List[Subscriber] = []

    def add_subscriber(self, subscriber):
        print("Publisher: Attached an subscriber.")
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscriber(self):
        print("Publisher: Notifying subscribers...")
        for subscriber in self.subscribers:
            subscriber.update(self)

    def some_logic(self):
        print("\nPublisher: I'm doing something important.")
        self.state = randint(0, 9)

        print(f"Publisher: My state has just changed to: {self.state}")
        self.notify_subscriber()


class Subscriber(ABC):

    @abstractmethod
    def update(self, publisher):
        pass


class ConcreteSubscriberA(Subscriber):
    def update(self, publisher):
        if publisher.state < 3:
            print("ConcreteSubscriberA: Reacted to the event")


class ConcreteSubscriberB(Subscriber):
    def update(self, publisher):
        if publisher.state == 0 or publisher.state >= 2:
            print("ConcreteSubscriberB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    publisher = ConcretePublisher()

    subscriber_a = ConcreteSubscriberA()
    publisher.add_subscriber(subscriber_a)

    subscriber_b = ConcreteSubscriberB()
    publisher.add_subscriber(subscriber_b)

    publisher.some_logic()
    publisher.some_logic()

    publisher.remove_subscriber(subscriber_a)

    publisher.some_logic()
