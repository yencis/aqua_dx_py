from ..common import API_ENDPOINT
from ..types import Game
from typing import Any
from urllib import parse
from .types import GameCard, Card
from pydantic import ValidationError
import logging
import requests

OPER = "card"
logger = logging.getLogger(__name__)


def get_user_card(username: str) -> Any:
    """
    Return card user information, uses the endpoint for `user-games`
    :param username: String of player username
    :return: Object
    :raises: ValidationError
    """
    response = requests.post(parse.urljoin(API_ENDPOINT, f"{OPER}/user-games"), params={"username": username})
    try:
        return Card.model_validate(response.json())
    except ValidationError as ve:
        logger.info("Unexpected error: %s", ve)
        raise ValidationError


def get_game_card(card: Card, game: Game) -> GameCard:
    """
    Return game specific card information
    :param game: Game
    :param card: Card object
    :return: GameCard
    """
    return getattr(card, game)
