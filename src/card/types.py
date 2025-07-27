from pydantic import BaseModel
from datetime import datetime


class GameCard(BaseModel):
    name: str
    rating: int
    lastLogin: datetime  # We can not verify a specific format because AquaDX does not use a specific format XD


class Card(BaseModel):
    mai2: GameCard | None = None
    chu3: GameCard | None = None
    ongeki: GameCard | None = None
    wacca: GameCard | None = None
    diva: GameCard | None = None
