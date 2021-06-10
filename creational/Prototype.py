import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Widget(Prototype):
    def __init__(self, width='None', height='None', display='None'):
        self.styles = {
            'width': width,
            'height': height,
            'display': display,
        }

    def __len__(self):
        return len(self.styles)

    def __getitem__(self, item):
        return self.styles[item]

    def __iter__(self):
        return self.styles.__iter__()


class Button(Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def main():
    b1 = Button()
    b1.styles.update({'display': 'block', 'width': '160px', 'height': '60px'})
    b2 = b1.clone()
    b2.styles.update({'display': 'None'})
    for key in b1:
        print('{key:8} -> {fo:^8} | {so:^8}'.format(key=key, fo=b1[key], so=b2[key]))


if __name__ == '__main__':
    main()
