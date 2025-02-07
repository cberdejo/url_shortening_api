import hashlib
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from services import save_url, get_url

def shorten_url(url: str, ttl: int = 3600):
    try:
        url_shortened = hashlib.md5(url.encode()).hexdigest()[:10]
        
        # Check for collisions
        if get_url(url_shortened):
            raise HTTPException(status_code=500, detail="Collision detected")

        url_saved = save_url(url, url_shortened, ttl)
        return JSONResponse(content={"code": 200, "message": "OK", "data": url_saved}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_original_url(url_shortened: str):
    try:
        url = await get_url(url_shortened)
        if url:
            return JSONResponse(content={"code": 200, "message": "OK", "data": url}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Not Found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
