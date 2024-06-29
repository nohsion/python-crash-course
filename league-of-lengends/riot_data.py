import configparser
from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class RiotAPIConfig:
    ACCOUNT_BY_RIOT_ID_URL: str
    SUMMONER_BY_UUID_URL: str
    LEAGUE_ENTRIES_BY_SUMMONER_ID_URL: str
    # OP.GG URL
    OPGG_SUMMONER_URL: str
    OPGG_CHAMPION_BUILD_URL: str
    # Data Dragon URL
    DDRAGON_PROFILE_ICON_URL: str
    DDRAGON_CHAMPION_URL: str
    DDRAGON_CHAMPION_IMG_URL: str

    @classmethod
    def from_config(cls, config_path: str = "config.ini", section: str = "RiotAPI"):
        config = configparser.ConfigParser()
        config.read(config_path)
        return cls(
            ACCOUNT_BY_RIOT_ID_URL=config.get(section, "accountByRiotId"),
            SUMMONER_BY_UUID_URL=config.get(section, "summonerByPUUID"),
            LEAGUE_ENTRIES_BY_SUMMONER_ID_URL=config.get(section, "leagueEntriesBySummonerId"),
            OPGG_SUMMONER_URL=config.get(section, "opggSummoner"),
            OPGG_CHAMPION_BUILD_URL=config.get(section, "opggChampionBuild"),
            DDRAGON_PROFILE_ICON_URL=config.get(section, "dd_profileicon"),
            DDRAGON_CHAMPION_URL=config.get(section, "dd_champion"),
            DDRAGON_CHAMPION_IMG_URL=config.get(section, "dd_champion_img")
        )

    @classmethod
    def get_latest_ddragon_version(cls) -> str:
        """
        Data Dragon API 버전 중 가장 최신 버전을 가져온다.
        https://developer.riotgames.com/docs/lol#data-dragon_versions
        """
        versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
        versions_res = requests.get(versions_url)
        if versions_res.status_code != 200:
            return "14.13.1"
        return versions_res.json()[0]


@dataclass(frozen=True)
class AccountDTO:
    """
    Get account by riot id
    https://developer.riotgames.com/apis#account-v1/GET_getByRiotId
    """
    puuid: str
    game_name: str
    tag_line: str

    @property
    def riot_id(self) -> str:
        return f"{self.game_name}#{self.tag_line}"


@dataclass(frozen=True)
class SummonerDTO:
    """
    Get a summoner by PUUID.
    https://developer.riotgames.com/apis#summoner-v4/GET_getByPUUID
    """
    account_id: str
    profile_icon_id: int
    revision_date: int
    id: str
    puuid: str
    summoner_level: int


@dataclass(frozen=True)
class MiniSeriesDTO:
    losses: int
    progress: str
    target: int
    wins: int


@dataclass(frozen=True)
class LeagueEntryDTO:
    """
    Get league entries in all queues for a given summoner ID
    https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner
    """
    league_id: str
    summoner_id: str
    queue_type: str
    tier: str
    rank: str
    league_points: int
    wins: int
    losses: int
    hot_streak: bool
    veteran: bool
    fresh_blood: bool
    inactive: bool
    mini_series: MiniSeriesDTO | None


@dataclass(frozen=True)
class ChampionInfoDTO:
    attack: int
    defense: int
    magic: int
    difficulty: int


@dataclass(frozen=True)
class ChampionImageDTO:
    full: str
    sprite: str
    group: str
    x: int
    y: int
    w: int
    h: int


@dataclass(frozen=True)
class ChampionStatsDTO:
    hp: int
    hpperlevel: int
    mp: int
    mpperlevel: int
    movespeed: int
    armor: int
    armorperlevel: float
    spellblock: int
    spellblockperlevel: float
    attackrange: int
    hpregen: float
    hpregenperlevel: float
    mpregen: float
    mpregenperlevel: float
    crit: int
    critperlevel: int
    attackdamage: int
    attackdamageperlevel: int
    attackspeedperlevel: float
    attackspeed: float


@dataclass(frozen=True)
class ChampionDTO:
    """
    챔피언 기본정보
    ex: https://ddragon.leagueoflegends.com/cdn/14.13.1/data/ko_KR/champion.json
    """
    id: str
    key: str
    name: str
    title: str
    blurb: str
    info: ChampionInfoDTO
    image: ChampionImageDTO
    tags: list[str]
    partype: str
    stats: ChampionStatsDTO
