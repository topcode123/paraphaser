from pydantic import BaseModel


class Paragraph(BaseModel):
    paragraph: str
