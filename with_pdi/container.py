from dependency_injector import containers, providers
from redis.asyncio import Redis
from . import service as service_layer, repository as repository_layer


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["with_pdi"],
    )
    config = providers.Configuration(json_files=["./config.json"])
    redis = providers.Singleton(
        Redis,
        host=config.redis_host,
        port=config.redis_port,
        password=config.redis_secret,
    )
    repository = providers.Factory(
        repository_layer.Repository,
        redis=redis,
    )
    service = providers.Factory(
        service_layer.Service,
        repository=repository,
    )
    singleton_service = providers.Singleton(
        service_layer.Service,
        repository=repository,
    )

def create_container():
    container = Container()
    return container
