from pydantic import BaseModel, WithJsonSchema
from typing import Annotated

class Song(BaseModel):
    composer: str
    genre: str
    name: str
    notes: Annotated[list[dict[str, float]], WithJsonSchema({"type":"object"})]
    ver: str
    song_id: Annotated[str | None, WithJsonSchema({"type": "text"})] = None  # Want this to remain optional for compatibility
