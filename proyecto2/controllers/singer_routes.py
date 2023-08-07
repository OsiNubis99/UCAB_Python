from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependency import get_db

from models.singer_models import Singer
from schemas.song_schemas import SongResponse
from schemas.singer_schemas import SingerCreate, SingerResponse

router = APIRouter(
    tags=["Singer"]
)

@router.get("/singers/", response_model=List[SingerResponse])
def get_singers(db: Session = Depends(get_db)):
    singers = db.query(Singer).all()
    return singers


@router.post("/singers/", response_model=SingerResponse)
def create_singer(singer: SingerCreate, db: Session = Depends(get_db)):
    new_singer = Singer(name=singer.name)
    db.add(new_singer)
    db.commit()
    db.refresh(new_singer)
    return new_singer


@router.get("/singers/{singer_id}/", response_model=SingerResponse)
def get_singer(singer_id: int, db: Session = Depends(get_db)):
    singer = db.query(Singer).filter(Singer.id == singer_id).first()
    if not singer:
        raise HTTPException(status_code=404, detail="Singer not found")
    return singer


@router.get("/singer/{id}/", response_model=List[SongResponse])
def get_song(id: int, db: Session = Depends(get_db)):
    singer = db.query(Singer).filter(Singer.id == id).first()
    if not singer:
        raise HTTPException(status_code=404, detail="Singer not found")
    if len(singer.albums) == 0:
        raise HTTPException(status_code=404, detail="Singer don't have any album")
    return [song for album in singer.albums for song in album.songs]
