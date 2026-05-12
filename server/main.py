from fastapi import FastAPI
from server.routes import router

app = FastAPI(title = 'test app')

app.include_router(router)
