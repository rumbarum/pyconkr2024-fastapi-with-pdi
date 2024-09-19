from setting_singleton import setting

redis = Redis(
    host=settings["redis_host"],
    port=settings["redis_port"],
    password=settings["redis_secret"],
)
