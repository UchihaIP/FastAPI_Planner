from fastapi import FastAPI
import uvicorn

from routes.events import event_router
from routes.users import user_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0",
                port=8080, reload=True)
