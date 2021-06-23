from abc import ABC, abstractmethod


class Command:
    @abstractmethod
    def execute(self):
        raise AttributeError('Method is not implement')

    @abstractmethod
    def undo(self):
        raise AttributeError('Method is not implement')


class EmptyCommand(Command):
    def execute(self):
        print('Command is not set')

    def undo(self):
        print('Nothing to do')


class Light:
    def on(self):
        print(f'Light {id(self)} turned on')

    def off(self):
        print(f'Light {id(self)} turned off')


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class Remote:
    def __init__(self, slot_num):
        cmnd = EmptyCommand()
        self.commands = [cmnd] * slot_num
        self.undos = []

    def set_command(self, command: Command, slot):
        self.commands[slot] = command

    def execute(self, slot):
        self.commands[slot].execute()
        self.undos.append(self.commands[slot].undo)

    def undo(self):
        if self.undos:
            command = self.undos.pop()
            command()


if __name__ == '__main__':
    l1 = Light()
    remote = Remote(10)
    remote.set_command(LightOnCommand(l1), 0)
    remote.set_command(LightOffCommand(l1), 1)
    remote.execute(0)
    remote.execute(1)
    remote.execute(2)
    remote.undo()
    remote.undo()
    remote.undo()
