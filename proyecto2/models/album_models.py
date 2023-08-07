from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config_db import Base

class Album(Base):
    __tablename__ = "album"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    singer_id = Column(Integer, ForeignKey("singer.id"))

    songs = relationship("Song", back_populates="album")
    singer = relationship("Singer", back_populates="albums")
