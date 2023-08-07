from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependency import get_db

from models.album_models import Album
from models.singer_models import Singer
from schemas.album_schemas import AlbumCreate, AlbumResponse

router = APIRouter(
    tags=["Album"]
)

@router.get("/albums/{album_id}/", response_model=AlbumResponse)
def get_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@router.post("/albums/{singer_id}/albums/", response_model=AlbumResponse)
def create_album(singer_id: int, album: AlbumCreate, db: Session = Depends(get_db)):
    singer = db.query(Singer).filter(Singer.id == singer_id).first()
    if not singer:
        raise HTTPException(status_code=404, detail="Singer not found")
    new_album = Album(name=album.name, singer_id=singer_id)
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album
