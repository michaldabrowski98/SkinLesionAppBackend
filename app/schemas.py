from pydantic import BaseModel

class SkinLesion(BaseModel):
    id: int
    code: str
    english_name: str
    polish_name: str
    description: str

class Image(BaseModel):
    name: str
    content: str
