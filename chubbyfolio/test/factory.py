from typing import Type


class CycleFactory:
    def __init__(self, factory: 'Type[Factory]', count: int):
        self.factory = factory
        self.count = count

    def __getattr__(self, name):
        if hasattr(self.factory, name):
            return lambda *args, **kwargs: [
                getattr(self.factory, name)(*args, **kwargs) for _ in range(0, self.count)
            ]


class Factory:
    @classmethod
    def cycle(cls, count):
        """
        Run given method X times:
            Factory.cycle(5).orderItem()  # gives 5 orders
        """
        return CycleFactory(cls, count)
