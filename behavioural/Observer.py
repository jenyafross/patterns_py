from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


class CurrenciesRowWidget(Observer):
    def __init__(self):
        self.data = {}

    def update(self, data):
        self.data.update(data)
        self.show_currencies()

    def show_currencies(self):
        output = ''
        for key, value in self.data.items():
            output += f'{key} - {value}\t|\t'
        print(output)


class CurrenciesColumnWidget(Observer):
    def __init__(self):
        self.data = {}

    def update(self, data):
        self.data.update(data)
        self.show_currencies()

    def show_currencies(self):
        output = '*' * 20 + '\n'
        for key, value in self.data.items():
            output += f'{key} - {value}\n'
        print(output)


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Currencies(Subject):
    def __init__(self):
        self.observers = []
        self.data = {}

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.data)

    def set_state(self, state):
        self.data.update(state)
        self.notify()


if __name__ == '__main__':
    currencies = Currencies()
    crw = CurrenciesRowWidget()
    ccw = CurrenciesColumnWidget()
    currencies.attach(crw)
    currencies.attach(ccw)
    currencies.set_state({'USD': 72.3, 'EUR': 90, 'UAH': 3.36})
    currencies.set_state({'USD': 72.5})
    currencies.set_state({'EUR': 92.7})
    currencies.set_state({'UAH': 3.64})
