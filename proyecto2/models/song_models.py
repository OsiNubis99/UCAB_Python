from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config_db import Base

class Song(Base):
    __tablename__ = "song"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    genre = Column(String(50))
    media_type = Column(String(50))
    album_id = Column(Integer, ForeignKey("album.id"))

    album = relationship("Album", back_populates="songs")
