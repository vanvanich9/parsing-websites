from pydantic import BaseModel


class ParsingElement(BaseModel):
    word: str
    value: int


class ParsingElementData(BaseModel):
    elements: list[ParsingElement] 