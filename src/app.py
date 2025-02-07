from fastapi import FastAPI
from bd import init_db
from routes import router


init_db()

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", reload=True)