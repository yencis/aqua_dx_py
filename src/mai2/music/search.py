import requests
import json
import logging
from urllib import parse
from .types import Song

logger = logging.getLogger(__name__)


class MusicSearch:
    LOADED = False
    ONLINE_MUSIC = {}
    LOCAL_MUSIC = {}

    def _load_online(self):
        response = requests.get("https://aquadx.net/d/mai2/00/all-music.json")
        if response.status_code != 200:
            raise IOError
        self.ONLINE_MUSIC = response.json()
        self.LOADED = True

    def _load_local(self):
        try:
            with open("data/all_music.json", mode='r', encoding='utf-8') as f:
                self.LOCAL_MUSIC = json.load(f)
        except OSError as oe:
            logger.info("Unable to load utils: %s", oe)
            self.LOCAL_MUSIC = {}

    def __init__(self, autoload=False):
        """
        Initialize MusicSearch instance
        :param autoload: If True, retrieves utils list from `https://aquadx.net/d/mai2/00/all-music.json`,
        otherwise uses local copy of JSON
        """
        if autoload:
            try:
                self._load_online()
            except IOError:
                self._load_local()
        else:
            self._load_local()

    def search(self, query: str, force=False) -> Song:
        """
        Search for utils
        :param query: Music ID as string
        :param force: If True, use ONLINE list instead of LOCAL list
        :return: Object
        """
        if self.LOADED:
            return Song.model_validate(self.ONLINE_MUSIC[query])
        else:
            if query not in self.LOCAL_MUSIC:
                if force:  # maybe not up to date
                    self._load_online()
                    return Song.model_validate(self.ONLINE_MUSIC[query])
                else:
                    raise KeyError("Song not found")
            else:
                return Song.model_validate(self.LOCAL_MUSIC[query])


class ImageSearch:

    URL_BASE = "https://aquadx.net/d/mai2/music"

    @staticmethod
    def get_image_id(song_id: str):
        # Dude I have no idea why the song_ids are like this
        if len(song_id) == 6:
            song_id = song_id[1:]

        if len(song_id) == 5:
            image_id = "00" + song_id[1:]
        else:
            image_id = "0" * (6 - len(song_id)) + song_id
        return image_id

    @staticmethod
    def get_image_url(song_id: str):
        return ImageSearch.URL_BASE + f"/{ImageSearch.get_image_id(song_id)}.png"
