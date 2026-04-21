from pydantic import BaseModel

class NotificationCreate(BaseModel):
    message: str


class NotificationResponse(BaseModel):
    id: int
    message: str
    is_read: bool

    class Config:
        from_attributes = True