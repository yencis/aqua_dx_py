from ..common import API_ENDPOINT
from ..types import Game
from .types import PlayerSummary
from urllib import parse
from pydantic import ValidationError
import logging
import requests


OPER = "game"
logger = logging.getLogger(__name__)


def get_summary(username: str, game: Game) -> PlayerSummary:
    """
    Get user summary based on chosen game (currently only Maimai support). Uses endpoint for `user-summary`
    :param username: player username
    :param game: Game (only Maimai is implemented)
    :return: PlayerSummary
    :raises: ValidationError
    """
    response = requests.post(parse.urljoin(API_ENDPOINT, f"{OPER}/{game}/user-summary"), params={"username": username})
    try:
        return PlayerSummary.model_validate(response.json(), context={"game": Game.MAI2})
    except ValidationError as ve:
        logger.info("Unexpected error: %s", ve)
        raise ValidationError
