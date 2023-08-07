from pydantic import BaseModel

class AlbumBase(BaseModel):
    name: str


class AlbumCreate(AlbumBase):
    pass


class AlbumResponse(AlbumBase):
    id: int
    singer_id: int

    class Config:
        from_attributes = True