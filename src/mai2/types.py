from pydantic import BaseModel, field_validator
from src.mai2.music.types import Song


class RatingPlayReadable(BaseModel):
    song: Song
    rating: int
    difficulty: float
    rank: str
    achievement: float


class RecentPlayReadable(BaseModel):
    song: Song
    rating: int
    rank: str
    achievement: float
    difficulty: float


class RatingPlay(BaseModel):
    song_id: str
    song_index: int
    version: int
    achievement: int

    @field_validator('song_index', 'version', 'achievement', mode='before')
    @classmethod
    def stringify(cls, v: str) -> int:
        """
        Allow fields to be input as strings assuming they can be cast to integers,
        will throw ValidationError if they can not be cast
        """
        return int(v)


class RatingComposition(BaseModel):
    best15: str
    best35: str


class RecentScore(BaseModel):
    # I had ChatGPT generate this from an input JSON so if it doesn't work blame that
    orderId: int
    playlogId: int
    version: int
    placeId: int
    placeName: str
    loginDate: int
    playDate: str
    userPlayDate: str
    type: int
    musicId: int
    level: int
    trackNo: int
    vsMode: int
    vsUserName: str
    vsStatus: int
    vsUserRating: int
    vsUserAchievement: int
    vsUserGradeRank: int
    vsRank: int
    playerNum: int
    playedUserId1: int
    playedUserName1: str
    playedMusicLevel1: int
    playedUserId2: int
    playedUserName2: str
    playedMusicLevel2: int
    playedUserId3: int
    playedUserName3: str
    playedMusicLevel3: int
    characterId1: int
    characterLevel1: int
    characterAwakening1: int
    characterId2: int
    characterLevel2: int
    characterAwakening2: int
    characterId3: int
    characterLevel3: int
    characterAwakening3: int
    characterId4: int
    characterLevel4: int
    characterAwakening4: int
    characterId5: int
    characterLevel5: int
    characterAwakening5: int
    achievement: int
    deluxscore: int
    scoreRank: int
    maxCombo: int
    totalCombo: int
    maxSync: int
    totalSync: int
    tapCriticalPerfect: int
    tapPerfect: int
    tapGreat: int
    tapGood: int
    tapMiss: int
    holdCriticalPerfect: int
    holdPerfect: int
    holdGreat: int
    holdGood: int
    holdMiss: int
    slideCriticalPerfect: int
    slidePerfect: int
    slideGreat: int
    slideGood: int
    slideMiss: int
    touchCriticalPerfect: int
    touchPerfect: int
    touchGreat: int
    touchGood: int
    touchMiss: int
    breakCriticalPerfect: int
    breakPerfect: int
    breakGreat: int
    breakGood: int
    breakMiss: int
    isTap: bool
    isHold: bool
    isSlide: bool
    isTouch: bool
    isBreak: bool
    isCriticalDisp: bool
    isFastLateDisp: bool
    fastCount: int
    lateCount: int
    isAchieveNewRecord: bool
    isDeluxscoreNewRecord: bool
    comboStatus: int
    syncStatus: int
    isClear: bool
    beforeRating: int
    afterRating: int
    beforeGrade: int
    afterGrade: int
    afterGradeRank: int
    beforeDeluxRating: int
    afterDeluxRating: int
    isPlayTutorial: bool
    isEventMode: bool
    isFreedomMode: bool
    playMode: int
    isNewFree: bool
    trialPlayAchievement: int
    extNum1: int
    extNum2: int
    extNum4: int
    extBool1: bool
    extBool2: bool
    extBool3: bool
    isFullCombo: bool
    isAllPerfect: bool
