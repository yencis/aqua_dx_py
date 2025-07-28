from src.game.types import PlayerSummary
from src.game.game import get_summary
from src.card import card
from .types import RatingPlay, RatingComposition, RatingPlayReadable, RecentScore, RecentPlayReadable
from collections import namedtuple
from src.mai2.music.search import MusicSearch
from ..types import Game

RFPair = namedtuple('RFPair', ['rank', 'factor'])

# I think these are arbitrary, so I'm hard-coding this in
ACHIEVEMENT_MAP = {
    1005000: RFPair("SSS+", 0.224),
    1000000: RFPair("SSS", 0.216),
    995000: RFPair("SS+", 0.211),
    990000: RFPair("SS", 0.208),
    980000: RFPair("S+", 0.203),
    970000: RFPair("S", 0.2),
    940000: RFPair("AAA", 0.168),
    900000: RFPair("AA", 0.152),
    800000: RFPair("A", 0.136),
    750000: RFPair("BBB", 0.120),
    700000: RFPair("BB", 0.112),
    600000: RFPair("B", 0.096),
    500000: RFPair("C", 0.08),
    400000: RFPair("D", 0.064),
    300000: RFPair("D", 0.048),
    200000: RFPair("D", 0.032),
    100000: RFPair("D", 0.016),
    0: RFPair("F", 0)
}


def get_maimai_summary(username: str):
    """
    Player summary but specifically for Maimai
    :param username: username
    :return: player summary
    """
    return get_summary(username=username, game=Game.MAI2)


def get_maimai_user_card(username: str):
    """
    Player card but specifically for Maimai
    :param username: username
    :return: player summary
    """
    return card.get_game_card(card=card.get_user_card(username), game=Game.MAI2)


def get_rank_factor(achievement: int) -> RFPair:
    for k, v in ACHIEVEMENT_MAP.items():  # assume ordered
        if achievement >= k:
            return v


def get_rating(factor: float, achievement: int, level: float) -> int:
    return int(factor * min(achievement / 10000., 100.5) * level)


def get_ratings(summary: PlayerSummary) -> tuple[list[RatingPlay], list[RatingPlay]]:
    """
    Get ratings
    :param summary:
    :return:
    """
    def process_best(best: str) -> list[RatingPlay]:
        return [RatingPlay.model_validate(dict(zip(["song_id", "song_index", "version", "achievement"], s.split(":"))))
                for s in best.split(",")]

    if isinstance(summary.ratingComposition, RatingComposition):
        return process_best(summary.ratingComposition.best15), process_best(summary.ratingComposition.best35)
    else:
        raise ValueError("Not a Maimai PlayerSummary")


def view_rating_play(play: RatingPlay, ms: MusicSearch, force=False) -> RatingPlayReadable:
    song = ms.search(play.song_id, force=force)
    rf_pair = get_rank_factor(play.achievement)
    difficulty = song.notes[play.song_index]["lv"]
    rating = get_rating(rf_pair.factor, play.achievement, difficulty)
    return RatingPlayReadable(song=song,
                              rating=rating,
                              difficulty=difficulty,
                              rank=rf_pair.rank,
                              achievement=play.achievement/10000.)


def view_recent_score(recent: RecentScore, ms: MusicSearch, force=False) -> RecentPlayReadable:
    song = ms.search(str(recent.musicId), force=force)
    rf_pair = get_rank_factor(recent.achievement)
    difficulty = song.notes[recent.level]["lv"]
    rating = get_rating(rf_pair.factor, recent.achievement, difficulty)
    return RecentPlayReadable(song=song,
                              rating=rating,
                              difficulty=difficulty,
                              rank=rf_pair.rank,
                              achievement=recent.achievement/10000.)
