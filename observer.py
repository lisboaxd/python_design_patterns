class Observer:
    '''Observer object
    it receive notifications of the observable object (Bird)
    '''

    def __init__(self, name) -> None:
        self.name = name

    def update(self, message):
        print(f'|{self.name} \treceived | {message}')


class Bird:
    '''Observable object
    it has the responsibility to notify the own observers
    '''

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)


mateus = Observer('Mateus')
william = Observer('William')
patrick = Observer('Patrick')

bird = Bird()
bird.add_observer(mateus)
bird.add_observer(william)
bird.add_observer(patrick)

bird.notify_observers("I'm flying")
