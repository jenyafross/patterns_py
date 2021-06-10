from abc import ABC, abstractmethod


class Widget(ABC):
    """
    Interface for all UI widgets
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        print(self.__class__.__base__.__name__, self.__class__.__name__)

    def width(self):
        return self.__width

    def height(self):
        return self.__height


class Scroll(Widget):
    """
    Interface for scroll widgets
    """

    def __init__(self):
        super(Scroll, self).__init__()
        self.__offset = 0

    def offset(self):
        return self.__offset


class Button(Widget):
    """
    Interface for button widgets
    """

    def __init__(self, state='init'):
        super().__init__()
        self.__state = state

    def state(self):
        return self.__state


class WidgetBuilder(ABC):
    """
    Abstract Factory
    """

    @abstractmethod
    def create_scroll(self) -> Scroll:
        pass

    @abstractmethod
    def create_button(self) -> Button:
        pass


class LightScroll(Scroll):
    pass


class LightButton(Button):
    pass


class LightThemeBuilder(WidgetBuilder):
    """
    Concrete Factory
    """

    def create_scroll(self):
        return LightScroll()

    def create_button(self):
        return LightButton()


class DarkScroll(Scroll):
    pass


class DarkButton(Button):
    pass


class DarkThemeBuilder(WidgetBuilder):
    """
    Concrete Factory
    """

    def create_scroll(self) -> Scroll:
        return DarkScroll()

    def create_button(self) -> Button:
        return DarkButton()


def main():
    theme_builders = {
        'light': LightThemeBuilder,
        'dark': DarkThemeBuilder,
    }
    ui_builder: WidgetBuilder = theme_builders['light']()
    button: Button = ui_builder.create_button()
    scroll: Scroll = ui_builder.create_scroll()

    ui_builder = theme_builders['dark']()
    button = ui_builder.create_button()
    scroll = ui_builder.create_scroll()


if __name__ == '__main__':
    main()
