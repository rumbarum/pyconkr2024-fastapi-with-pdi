
class Engine:
    def get_power(self):
        ...

# before
class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        power = self.engine.get_power()
        # do something with power

car = Car()


# after
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def drive(self):
        self.engine.get_power()
        # do something with power

engine = Engine()
car = Car(engine=engine)
