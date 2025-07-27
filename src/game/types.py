from pydantic import BaseModel, ValidationInfo, field_validator, ValidationError
from ..common import GAME_TYPE_MAPPING
from datetime import datetime
from typing import Any
from ..types import Game


class AquaUser(BaseModel):
    # TODO: make this an Enum
    country: str
    displayName: str
    profileBio: str
    profileLocation: str
    profilePicture: str  # https://aquadx.net/aqua/uploads/net/portrait/
    regTime: float  # In units of Milliseconds
    username: str


class PlayerSummary(BaseModel):  # I think this is the same for all games, but I have not checked
    accuracy: float
    allPerfect: int
    aquaUser: AquaUser | None = None
    detailedRanks: Any  # Game Dependent
    fullCombo: int
    joined: datetime
    lastPlayedHost: str | None = None
    lastSeen: datetime
    lastVersion: str
    maxCombo: int
    name: str
    plays: int
    ranks: Any
    rating: int
    ratingComposition: Any  # Game Dependent
    ratingHighest: int
    recent: list[Any]  # Game Dependent
    rival: Any
    serverRank: int
    totalPlayTime: int
    totalScore: int

    @field_validator('ratingComposition', mode='after')
    @classmethod
    def verify_game_composition(cls, v: Any, info: ValidationInfo) -> Any:
        # Ensure that ratingComposition matches the game context passed, if no context passed ignore
        if isinstance(info.context, dict) and "game" in info.context:
            game = info.context["game"]
            if isinstance(game, Game):
                # Note: we don't warn the user if the game is not supported
                return GAME_TYPE_MAPPING[game].RatingComposition.model_validate(v) if game in GAME_TYPE_MAPPING else v
            else:
                raise ValueError("Unknown Game")
        else:
            return v


    @field_validator('recent', mode='after')
    @classmethod
    def verify_recent(cls, v: list[Any], info: ValidationInfo) -> list[Any]:
        # Ensure that ratingComposition matches the game context passed, if no context passed ignore
        if isinstance(info.context, dict) and "game" in info.context:
            game = info.context["game"]
            if isinstance(game, Game):
                # Note: we don't warn the user if the game is not supported
                return [GAME_TYPE_MAPPING[game].RecentScore.model_validate(v_s) for v_s in v] if game in GAME_TYPE_MAPPING else v
            else:
                raise ValueError("Unknown Game")
        else:
            return v
