from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine
from controllers.album_routes import router as album_router
from controllers.singer_routes import router as singer_router
from controllers.song_routes import router as song_router

def get_application():
    # crea la base de datos
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="Proyecto 2", version="1.0.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(album_router, prefix="/music-store/api/v1")
    app.include_router(singer_router, prefix="/music-store/api/v1")
    app.include_router(song_router, prefix="/music-store/api/v1")
    return app

app = get_application()

@app.get("/music-store/api/v1/")
def home() -> dict:
    return {"mensaje": "Bienvenido a mi proyecto 2"}