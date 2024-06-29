import configparser
from dataclasses import dataclass


@dataclass(frozen=True)
class RiotAPIConfig:
    ACCOUNT_BY_RIOT_ID_BASEURL: str
    SUMMONER_BY_UUID_BASEURL: str
    LEAGUE_ENTRIES_BY_SUMMONER_ID_BASEURL: str

    @classmethod
    def from_config(cls, config_path: str = "config.ini", section: str = "RiotAPI"):
        config = configparser.ConfigParser()
        config.read(config_path)
        return cls(
            ACCOUNT_BY_RIOT_ID_BASEURL=config.get(section, "accountByRiotId"),
            SUMMONER_BY_UUID_BASEURL=config.get(section, "summonerByPUUID"),
            LEAGUE_ENTRIES_BY_SUMMONER_ID_BASEURL=config.get(section, "leagueEntriesBySummonerId"),
        )


@dataclass(frozen=True)
class AccountDTO:
    """
    Get account by riot id
    https://developer.riotgames.com/apis#account-v1/GET_getByRiotId
    """
    puuid: str
    game_name: str
    tag_line: str


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
