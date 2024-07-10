from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbic'
        from_attributes = True