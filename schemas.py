from pydantic import BaseModel


class BookIn(BaseModel):
    title: str
    author: str
    isbn: str
    published_year: int
    copies: int = 1


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_year: int | None = None
    copies: int | None = None


class BookOut(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    published_year: int
    copies: int

    class Config:
        from_attributes = True