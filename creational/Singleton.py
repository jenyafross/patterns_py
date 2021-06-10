class SingletonBase:
    """
    Base class singleton
    """
    __instance = None
    text = 'I\'m a Base class Singleton'

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


def singleton(klass):
    instances = {}

    def wrapped(*args, **kwargs):
        if klass not in instances:
            instances[klass] = klass(*args, **kwargs)
        return instances[klass]

    return wrapped


@singleton
class DecoSingleton:
    text = 'I\'m a DecoSingleton'


class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class MySingleton(metaclass=MetaSingleton):
    def __init__(self):
        self.text = 'I\'m a Meta Singleton class'


b1 = SingletonBase()
b2 = SingletonBase()
print(b1.text)
b1.text = 'Changed Base class Singleton'
print(b2.text)
print(id(b1) == id(b2))

d1 = DecoSingleton()
d2 = DecoSingleton()
print(d1.text)
d1.text = 'Changed DecoSingleton text'
print(d2.text)
print(id(d1) == id(d2))

m1 = MySingleton()
m2 = MySingleton()
print(m1.text)
m1.text = 'Changed Meta class Singleton'
print(m2.text)
print(id(m1) == id(m2))
