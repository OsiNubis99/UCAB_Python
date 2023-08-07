from pydantic import BaseModel

class SongBase(BaseModel):
    name: str
    genre: str
    media_type: str


class SongCreate(SongBase):
    pass


class SongResponse(SongBase):
    id: int
    album_id: int

    class Config:
        from_attributes = True