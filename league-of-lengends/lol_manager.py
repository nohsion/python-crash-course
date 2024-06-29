import os
import requests
from dotenv import load_dotenv
from typing import Set

from riot_data import RiotAPIConfig, AccountDTO, SummonerDTO, LeagueEntryDTO, MiniSeriesDTO
from common import logger


class LolManager:
    def __init__(self):
        # Load env
        load_dotenv()
        self.RIOT_API_KEY: str = os.getenv("RIOT_API_KEY")

        # Load config
        self.riot_conf: RiotAPIConfig = RiotAPIConfig.from_config()

    def get_account_by_name_and_tag(self, name: str, tag: str) -> AccountDTO:
        """
        RiotId("name#tag")로부터 account 정보를 가져온다. (주요 정보: puuid)
        """
        account_by_riot_id_url: str = f"{self.riot_conf.ACCOUNT_BY_RIOT_ID_URL}/{name}/{tag}"
        account_res = requests.get(account_by_riot_id_url, headers={"X-Riot-Token": self.RIOT_API_KEY})
        if account_res.status_code != 200:
            logger.error(f"Error searching for summoner {name}#{tag}")
            raise Exception(f"Error searching for summoner {name}#{tag}")
        res_data: dict = account_res.json()
        logger.info(f"API: Account data={res_data}")
        return AccountDTO(
            puuid=res_data["puuid"],
            game_name=res_data["gameName"],
            tag_line=res_data["tagLine"],
        )

    def get_summoner_by_puuid(self, puuid: str) -> SummonerDTO:
        """
        puuid로부터 소환사 정보를 가져온다.
        """
        summoner_by_puuid_url: str = f"{self.riot_conf.SUMMONER_BY_UUID_URL}/{puuid}"
        summoner_res = requests.get(summoner_by_puuid_url, headers={"X-Riot-Token": self.RIOT_API_KEY})
        if summoner_res.status_code != 200:
            logger.error(f"Error searching for summoner with puuid {puuid}")
            raise Exception(f"Error searching for summoner with puuid {puuid}")
        res_data: dict = summoner_res.json()
        logger.info(f"API: Summoner data={res_data}")
        return SummonerDTO(
            account_id=res_data["accountId"],
            profile_icon_id=res_data["profileIconId"],
            revision_date=res_data["revisionDate"],
            id=res_data["id"],
            puuid=res_data["puuid"],
            summoner_level=res_data["summonerLevel"],
        )

    def get_league_entries_by_summoner_id(self, summoner_id: str) -> Set[LeagueEntryDTO]:
        """
        소환사 ID에 대한 리그 정보를 가져온다.
        """
        league_entries_by_summoner_id_url: str = f"{self.riot_conf.LEAGUE_ENTRIES_BY_SUMMONER_ID_URL}/{summoner_id}"
        league_entries_res = requests.get(league_entries_by_summoner_id_url, headers={"X-Riot-Token": self.RIOT_API_KEY})
        if league_entries_res.status_code != 200:
            logger.error(f"Error searching for league entries with summoner id {summoner_id}")
            raise Exception(f"Error searching for league entries with summoner id {summoner_id}")
        res_data: list[dict] = league_entries_res.json()
        logger.debug(f"API: League entries data={res_data}")
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

    @staticmethod
    def find_league_entry_by_queue_type(
            league_entries: Set[LeagueEntryDTO],
            queue_type: str | None = None
    ) -> LeagueEntryDTO | None:
        """
        리그 정보 중에서 queue_type에 해당하는 첫번째 리그 정보를 가져온다.
        queue_type이 None이면 우선순위에 따라 선택한다 (솔로 랭크 > 팀 랭크).
        """
        if not league_entries:
            return None

        # queue_type을 지정하면, 해당 queue_type에 해당하는 첫 번째 리그 정보를 가져온다.
        if queue_type:
            return next((entry for entry in league_entries if entry.queue_type == queue_type), None)

        # queue_type을 지정하지 않으면, 솔랭(RANKED_SOLO_5x5) 리그 -> 자랭(RANKED_TEAM_5x5) 리그 순으로 가져온다.
        solo_ranked_entry = next((entry for entry in league_entries if entry.queue_type == "RANKED_SOLO_5x5"), None)
        if solo_ranked_entry:
            return solo_ranked_entry

        team_ranked_entry = next((entry for entry in league_entries if entry.queue_type == "RANKED_TEAM_5x5"), None)
        return team_ranked_entry
