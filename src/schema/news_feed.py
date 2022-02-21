from pydantic import BaseModel, validator


class NewsFeedRequest(BaseModel):
    title: str
    body: str
    userId: int

    class Config:
        orm_mode = True

class NewsFeedResponse(BaseModel):
    title: str
    body: str
    userId: int
    id: int
    # id2: int

    class Config:
        orm_mode = True
        validate_all = True

