from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config_db import Base

class Singer(Base):
    __tablename__ = "singer"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    albums = relationship("Album", back_populates="singer")
