from ..common import API_ENDPOINT
from ..types import Game
from typing import Any
from urllib import parse
from .types import GameCard, Card
from src.transport import http_requests
from pydantic import ValidationError
import logging

# import requests

logger = logging.getLogger(__name__)


class CardClient:
    def __init__(self):
        self.OPER = "card"
        self.requests = http_requests.HTTPRequest()

    def get_user_card(self, username: str) -> Any:
        """
        Return card user information, uses the endpoint for `user-games`
        :param username: String of player username
        :return: Object
        :raises: ValidationError
        """
        # response = requests.post(parse.urljoin(API_ENDPOINT, f"{OPER}/user-games"), params={"username": username})
        response = self.requests.perform_request("POST", parse.urljoin(API_ENDPOINT, f"{self.OPER}/user-games"),
                                                 params={"username": username})
        try:
            return Card.model_validate(response.json())
        except ValidationError as ve:
            logger.info("Unexpected error: %s", ve)
            raise ValidationError


    def get_game_card(self, card: Card, game: Game) -> GameCard:
        """
        Return game specific card information
        :param game: Game
        :param card: Card object
        :return: GameCard
        """
        return getattr(card, game)
