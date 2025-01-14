from bd import rdb


def save_url(url: str, shortened_url: str, ttl: int):
    rdb.set(shortened_url, url)
    rdb.expire(shortened_url, ttl)


def get_url(shortened_url: str):
    getResult = rdb.get(shortened_url)
    return getResult
