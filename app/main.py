# from app.api import notes, ping
from app.db import database, engine, metadata
from fastapi import FastAPI

from app.routes import user
metadata.create_all(engine)

app = FastAPI(    
		title="User API",
    	description="User API Documentation",
    	version="1.0.0",)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user.router, prefix = "/user", tags = ['user'])


# app.include_router(ping.router)
# app.include_router(notes.router, prefix="/notes", tags=["notes"])
