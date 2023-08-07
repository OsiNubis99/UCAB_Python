from pydantic import BaseModel

class SingerBase(BaseModel):
    name: str


class SingerCreate(SingerBase):
    pass


class SingerResponse(SingerBase):
    id: int

    class Config:
        from_attributes = True