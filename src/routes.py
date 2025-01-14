from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse

router = APIRouter()
from validators import checkAuhtorization, validateUrlIsPresentAndValid
from controllers import shorten_url, get_original_url


@router.post("/shorten")
async def shorten(request: Request, response: Response):
    url = (await request.json())["url"]
    api_key = request.headers.get("X-Api-Key")
    authorized = checkAuhtorization(api_key)

    if not authorized:
        return Response(
            content="Unauthorized", status_code=403, media_type="application/json"
        )

    if not validateUrlIsPresentAndValid(url):
        return Response(
            content="Invalid URL",
            status_code=400,
            media_type="application/json",
        )

    res = shorten_url(url)
    return Response(
        content=res["message"], status_code=res["code"], media_type="application/json"
    )


@router.get("/goTo/{url_shortened}")
async def redirect_url(url_shortened: str, response: Response):
    res = await get_original_url(url_shortened)
    if res["code"] == 200:
        return RedirectResponse(url=res["data"])
    else:
        return Response(
            content=res["message"],
            status_code=res["code"],
            media_type="application/json",
        )
