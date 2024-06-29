import logging
import os
import requests
from dotenv import load_dotenv

from riot_data import RiotAPIConfig, AccountDTO, SummonerDTO, LeagueEntryDTO, MiniSeriesDTO

# Load env
load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_KEY")

# Load config
riot_conf: RiotAPIConfig = RiotAPIConfig.from_config()

# Init logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_account_by_name_and_tag(name: str, tag: str) -> AccountDTO:
    """
    RiotId("name#tag")로부터 account 정보를 가져온다. (주요 정보: puuid)
    """
    account_by_riot_id_url: str = f"{riot_conf.ACCOUNT_BY_RIOT_ID_BASEURL}/{name}/{tag}"
    account_res = requests.get(account_by_riot_id_url, headers={"X-Riot-Token": RIOT_API_KEY})
    if account_res.status_code != 200:
        logger.error(f"Error searching for summoner {name}#{tag}")
        raise Exception(f"Error searching for summoner {name}#{tag}")
    res_data: dict = account_res.json()
    logger.info(f"Account data={res_data}")
    return AccountDTO(
        puuid=res_data["puuid"],
        game_name=res_data["gameName"],
        tag_line=res_data["tagLine"],
    )


def get_summoner_by_puuid(puuid: str) -> SummonerDTO:
    """
    puuid로부터 소환사 정보를 가져온다.
    """
    summoner_by_puuid_url: str = f"{riot_conf.SUMMONER_BY_UUID_BASEURL}/{puuid}"
    summoner_res = requests.get(summoner_by_puuid_url, headers={"X-Riot-Token": RIOT_API_KEY})
    if summoner_res.status_code != 200:
        logger.error(f"Error searching for summoner with puuid {puuid}")
        raise Exception(f"Error searching for summoner with puuid {puuid}")
    res_data: dict = summoner_res.json()
    logger.info(f"Summoner data={res_data}")
    return SummonerDTO(
        account_id=res_data["accountId"],
        profile_icon_id=res_data["profileIconId"],
        revision_date=res_data["revisionDate"],
        id=res_data["id"],
        puuid=res_data["puuid"],
        summoner_level=res_data["summonerLevel"],
    )


def get_league_entries_by_summoner_id(summoner_id: str) -> set[LeagueEntryDTO]:
    """
    소환사 ID에 대한 리그 정보를 가져온다.
    """
    league_entries_by_summoner_id_url: str = f"{riot_conf.LEAGUE_ENTRIES_BY_SUMMONER_ID_BASEURL}/{summoner_id}"
    league_entries_res = requests.get(league_entries_by_summoner_id_url, headers={"X-Riot-Token": RIOT_API_KEY})
    if league_entries_res.status_code != 200:
        logger.error(f"Error searching for league entries with summoner id {summoner_id}")
        raise Exception(f"Error searching for league entries with summoner id {summoner_id}")
    res_data: list[dict] = league_entries_res.json()
    logger.debug(f"League entries data={res_data}")
    return {
        LeagueEntryDTO(
            league_id=entry["leagueId"],
            summoner_id=entry["summonerId"],
            queue_type=entry["queueType"],
            tier=entry["tier"],
            rank=entry["rank"],
            league_points=entry["leaguePoints"],
            wins=entry["wins"],
            losses=entry["losses"],
            hot_streak=entry["hotStreak"],
            veteran=entry["veteran"],
            fresh_blood=entry["freshBlood"],
            inactive=entry["inactive"],
            mini_series=MiniSeriesDTO(
                losses=entry["miniSeries"]["losses"],
                progress=entry["miniSeries"]["progress"],
                target=entry["miniSeries"]["target"],
                wins=entry["miniSeries"]["wins"],
            ) if "miniSeries" in entry else None
        ) for entry in res_data
    }


if __name__ == '__main__':
    account: AccountDTO = get_account_by_name_and_tag("용맹한시온이", "KR1")
    summoner: SummonerDTO = get_summoner_by_puuid(account.puuid)
    print(f'summoner: {summoner}')
    league_entry: set[LeagueEntryDTO] = get_league_entries_by_summoner_id(summoner.id)
    print(f'league_entry: {league_entry}')
