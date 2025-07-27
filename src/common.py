from .types import Game
import importlib

API_ENDPOINT = "https://aquadx.net/aqua/api/v2/"
MAI2_TYPES_MODULE = importlib.import_module("src.mai2.types")  # manually import to avoid dependency issues


GAME_TYPE_MAPPING = {
    # Supported games, allow all packages to reference models of different games without dealing with
    # cyclic dependencies
    Game.MAI2: MAI2_TYPES_MODULE
}
