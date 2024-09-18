# 엔진 diesel 타입 추가
class Engine:
    ...
class DieselEngine:
    ...

car = Car(engine=Engine())
diesel_car = Car(engine=DieselEngine())

# 함수에 객체 생성 묶음
def make_car() -> Car:
    return Car(engine=Engine())

def make_diesel_car() -> Car:
    return Car(engine=DiselEngine())

car = make_car()
diesel_car = make_diesel_car()


# 동일 의존성 개별 함수로 분리
def make_engine() -> Engine:
    return Engine()

def make_diesel_engine() -> DieselEngine:
    return DieselEngine()

def make_car(make_engine: Callable = make_engine) -> Car:
    return Car(engine=make_engine())

car = make_car()
diesel_car = make_car(make_engine=make_disel_engine)


# 의존성 체인 추가
def get_high_price_oil() -> str:
    return "HIGH_PRICE"

def get_base_price_oil() -> str:
    return "LOW_PRICE"

def make_engine(get_oil: Callable = get_base_price_oil) -> Engine:
    return Engine(oil=get_oil())

def make_car(make_engine: Callable = make_engine) -> Car:
    return Car(engine=make_engine())

base_price_oil_car = make_car()

# 람다로 의존성 함수 전달
high_price_oil_engine_car = make_car(
    make_engine= lambda: make_engine(
        get_oil=get_high_price_oil
    )
)

# 또는 의존성 함수 분리
def make_high_price_oil_engine(
        get_oil: Callable = get_high_price_oil
) -> Engine:
    return Engine(oil=get_oil())

high_price_oil_engine_car = make_car(
    make_engine=make_high_price_oil_engine
)



# 특수 타입 생성
singleton_car = None
def make_singleton_car() -> Car:
    if singleton_car is None:
        singleton_car = Car(engine=Engine())
    return singleton_car
