
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependency import get_db

from models.album_models import Album
from models.song_models import Song
from schemas.song_schemas import SongCreate, SongResponse

router = APIRouter(
    tags=["Song"]
)

@router.get("/songs/{song_id}/", response_model=SongResponse)
def get_song(song_id: int, db: Session = Depends(get_db)):
    song = db.query(Song).filter(Song.id == song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@router.post("/songs/{album_id}/songs/", response_model=SongResponse)
def create_song(album_id: int, song: SongCreate, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    new_song = Song(name=song.name, genre=song.genre, media_type=song.media_type, album_id=album_id)
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song
