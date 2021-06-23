from abc import ABC, abstractmethod


class Executable(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Add(Executable):
    def execute(self, a, b):
        return a + b


class Subtract(Executable):
    def execute(self, a, b):
        return a - b


class Multiply(Executable):
    def execute(self, a, b):
        return a * b


class Strategy(ABC):
    def __init__(self):
        self.strategy: Executable = None

    def set_strategy(self, strategy: Executable):
        self.strategy = strategy

    @abstractmethod
    def execute(self, a, b):
        raise AttributeError('Method should be implement')


class ConcreteStrategy(Strategy):
    def execute(self, a, b):
        return self.strategy.execute(a, b)


if __name__ == '__main__':
    s1 = ConcreteStrategy()
    strategies = [Add, Subtract, Multiply]
    for strategy in strategies:
        s1.set_strategy(strategy())
        print(s1.execute(3, 4))
