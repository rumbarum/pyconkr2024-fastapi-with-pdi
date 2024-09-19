from redis.asyncio import Redis

from .repository import Repository
from .service import Service
import json

setting = None
def get_setting() -> dict:
    global setting
    if setting is None:
        with open("config.json") as f:
            setting = json.load(f)
    return setting

singleton_redis = None
def get_redis(get_setting=get_setting) -> Redis:
    setting = get_setting()
    global singleton_redis
    if singleton_redis is None:
        singleton_redis = Redis(
            host=setting["redis_host"],
            port=setting["redis_port"],
            password=setting["redis_secret"],
        )
    return singleton_redis

def get_repository(get_redis=get_redis) -> Repository:
    redis=get_redis()
    return Repository(redis=redis)

def get_service(get_repository=get_repository) -> Service:
    repository = get_repository()
    return Service(repository=repository)
