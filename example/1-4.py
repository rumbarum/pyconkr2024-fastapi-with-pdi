# 엔진 diesel 타입 추가
class Engine:
    ...

class DieselEngine:
   ...

# 의존성 주입을 하지 않은 경우
class Car:
    def __init__(self, type: str):
        if type == "diesel":
            self.engine = DieselEngine()
        else:
            self.engine = Engine()

    def drive(self):
        power = self.engine.get_power()
        # do something with power
        ...

car = Car()
diesel_car = Car(type="diesel")

# 의존성 주입을 한 경우
engine = Engine()
car = Car(engine=engine)

diesel_engine = DieselEngine()
diesel_car = Car(engine=diesel_engine)

# 함수로 객체 생성 묶음
def make_car() -> Car:
    engine = Engine()
    return Car(engine=engine)

def make_diesel_car() -> Car:
    engine = DieselEngine()
    return Car(engine=engine)

car = make_car()
diesel_car = make_diesel_car()


# 동일 의존성 개별 함수로 분리
def make_engine() -> Engine:
    return Engine()

def make_diesel_engine() -> DieselEngine:
    return DieselEngine()

def make_car(make_engine: Callable = make_engine) -> Car:
    engine = make_engine()
    return Car(engine=engine)

car = make_car()
diesel_car = make_car(make_engine=make_disel_engine)


# 동일 의존성 개별 함수로 분리 2
def make_engine(is_diesel=False) -> Engine:
    if is_diesel:
        return DieselEngine()
    return Engine()

def make_car(make_engine: Callable = make_engine) -> Car:
    engine = make_engine()
    return Car(engine=engine)

car = make_car()
diesel_car = make_car(make_engine= lambda: make_engine(is_diesel=True))


# Engine 의존성 추가
class Engine:
    def __init__(self, oil: Oil):
        self.oil = oil

def get_base_price_oil() -> Oil:
    return Oil(price="base")

def make_engine(get_oil: Callable = get_base_price_oil) -> Engine:
    oil = get_oil()
    return Engine(oil=oil)

def make_car(make_engine: Callable = make_engine) -> Car:
    engine = make_engine()
    return Car(engine=engine)

base_price_oil_car = make_car()


def get_high_price_oil() -> Oil:
    return Oil(price="high")

# 람다로 의존성 함수 전달
high_price_oil_engine_car = make_car(
    make_engine= lambda: make_engine(get_oil=get_high_price_oil)
)

# 또는 의존성 함수 분리
def make_high_price_oil_engine(get_oil: Callable = get_high_price_oil) -> Engine:
    oil = get_oil()
    return Engine(oil=oil)

high_price_oil_engine_car = make_car(make_engine=make_high_price_oil_engine)

# 또는 make_high_price_oil_car 함수 작성
def make_high_price_oil_car(make_engine: Callable=make_high_price_oil_engine) -> Car:
    engine = make_engine()
    return Car(engine=engine)

high_price_oil_engine_car = make_high_price_oil_car()



car = Car(
    engine=DieselEngine(
        oil=Oil(price="high")
    )
)

car = Car(
    engine=DieselEngine(
        oil=Oil(price="high"), fuel_addition=FuelAddition(grade="premium")
    )
)



# 싱글톤 diesel car
singleton_diesel_car = None
def make_singleton_car(make_engine: Callable = make_diesel_engine) -> Car:
    if singleton_car is None:
        engine = make_engine()
        singleton_diesel_car = Car(engine=engine)
    return singleton_car

# some_code.py
singleton_diesel_car = make_singleton_car()

# other_code.py
singleton_diesel_car = make_singleton_car()
