from abc import ABC, abstractmethod


# Product class
class Computer:
    def __init__(self, cpu, memory, storage, gpu):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"CPU: {self.cpu}, Memory: {self.memory}, Storage: {self.storage}, GPU: {self.gpu}"


# Builder interface
class ComputerBuilder(ABC):

    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_memory(self, memory):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def set_gpu(self, gpu):
        pass


# Concrete builder
class GamingComputerBuilder(ComputerBuilder):

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_memory(self, memory):
        self.memory = memory

    def set_storage(self, storage):
        self.storage = storage

    def set_gpu(self, gpu):
        self.gpu = gpu

    def build(self):
        return Computer(self.cpu, self.memory, self.storage, self.gpu)


# Director class
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, cpu, memory, storage, gpu):
        self.builder.set_cpu(cpu)
        self.builder.set_memory(memory)
        self.builder.set_storage(storage)
        self.builder.set_gpu(gpu)

        return self.builder.build()


# Client code
if __name__ == "__main__":
    gaming_computer_builder = GamingComputerBuilder()
    director = Director(gaming_computer_builder)

    gaming_pc = director.construct("Intel i7", "16GB", "1TB SSD", "Nvidia RTX 3080")

    print("Gaming PC specs:")
    print(gaming_pc)
