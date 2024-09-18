from redis.asyncio import Redis

from .repository import Repository
from .service import Service
import json

def get_setting() -> dict:
    with open("config.json") as f:
        json_cong = json.load(f)
    return json_cong

setting = get_setting()

def get_redis() -> Redis:
    return Redis(
        host=setting["redis_host"],
        port=setting["redis_port"],
        password=setting["redis_secret"],
    )

def get_repository(get_redis=get_redis) -> Repository:
    return Repository(redis=get_redis())

def get_service(get_repository=get_repository) -> Service:
    return Service(repository=get_repository())

global_service = None
def get_singleton_service(get_repository=get_repository) -> Service:
    global global_service
    if global_service is None:
        global_service = Service(repository=get_repository())
    return global_service
