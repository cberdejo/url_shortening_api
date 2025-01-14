import hashlib
from services import save_url, get_url


INITIAL_RES = {"code": 500, "message": "Internal Server Error", "data": None}


def shorten_url(url: str, ttl: int = 3600):
    res = INITIAL_RES.copy()
    try:
        url_shortened = hashlib.md5(url.encode()).hexdigest()[:10]
        # check for collisions
        while get_url(url_shortened):
            # if there is a collision, we will generate a new hash, ftm just return 500 error
            res = {"code": 500, "message": "Collision detected", "data": None}

        url_saved = save_url(url, url_shortened, ttl)
        print(url_shortened)
        res = {"code": 200, "message": "OK", "data": url_saved}
    except Exception as e:
        res = {"code": 500, "message": str(e), "data": None}
    return res


# save in bd


async def get_original_url(url_shortened: str):
    res = INITIAL_RES.copy()
    try:
        url = await get_url(url_shortened)
        if url:
            res = {"code": 200, "message": "OK", "data": url}
        else:
            res = {"code": 404, "message": "Not Found", "data": None}

    except Exception as e:
        res = {"code": 500, "message": str(e), "data": None}
    return res
