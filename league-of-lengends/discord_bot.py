import os
from typing import Set

import discord
from dotenv import load_dotenv
from discord.ext import commands

from common import logger
from lol_manager import LolManager
from riot_data import AccountDTO, SummonerDTO, LeagueEntryDTO


class DiscordBot:
    def __init__(
            self,
            lol_manager: LolManager,
            channel_id=os.getenv("DISCORD_LOL_BOT_CHANNEL_ID"),
    ):
        load_dotenv()
        self.discord_token: str = os.getenv("DISCORD_TOKEN")
        self.channel_id: str = channel_id
        self.lol_manager: LolManager = lol_manager

        self.bot: commands.Bot = self._create_bot()
        self._setup_events()
        self._setup_commands()

    @staticmethod
    def _create_bot() -> commands.Bot:
        intents = discord.Intents.default()
        intents.message_content = True
        return commands.Bot(command_prefix='!', intents=intents)

    def run(self):
        self.bot.run(self.discord_token)

    def _setup_events(self):
        @self.bot.event
        async def on_ready():
            logger.info(f'{self.bot.user} has connected to Discord!')
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name="!help"))

        @self.bot.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound):
                await ctx.send("알 수 없는 명령어입니다. !help를 입력해주세요.")

    def _setup_commands(self):
        @self.bot.command(name='안녕')
        async def cmd_help(ctx):
            await ctx.send("Help message")

        # !롤 소환사명#태그: 소환사의 기본정보를 확인합니다.
        @self.bot.command(name='롤')
        async def cmd_lol(ctx, *args):
            name, tag = args[0].split("#")
            await ctx.send(embed=self._get_lol_summoner_embed(name, tag))

    def _get_lol_summoner_embed(self, name: str, tag: str) -> discord.Embed:
        account_dto: AccountDTO = self.lol_manager.get_account_by_name_and_tag(name, tag)
        summoner_dto: SummonerDTO = self.lol_manager.get_summoner_by_puuid(account_dto.puuid)
        league_entry_dtos: Set[LeagueEntryDTO] = self.lol_manager.get_league_entries_by_summoner_id(summoner_dto.id)
        league_entry: LeagueEntryDTO = self.lol_manager.find_league_entry_by_queue_type(league_entry_dtos)

        if league_entry is None:
            embed = discord.Embed(
                title="Unranked",
                description="랭크 배치를 받으셔야겠네요!" if summoner_dto.summoner_level > 30 else "얼른 레벨 30부터 올려보세요!",
                color=0x0000ff
            )
        else:
            rank_type: str = '솔랭' if league_entry.queue_type == 'RANKED_SOLO_5x5' else '자랭'
            embed = discord.Embed(
                title=f"{rank_type}: {league_entry.tier} {league_entry.rank}",
                description="대단한 실력자네요!",
                color=0x00ff00
            )
        embed.set_author(
            name=account_dto.riot_id,
            url=self.lol_manager.riot_conf.OPGG_SUMMONER_URL.format(name=name, tag=tag.upper()),
            icon_url=self.lol_manager.riot_conf.PROFILE_ICON_URL.format(profileicon=summoner_dto.profile_icon_id)
        )
        embed.add_field(name="소환사 레벨", value=f"{summoner_dto.summoner_level} 레벨", inline=False)
        embed.add_field(name="리그 포인트", value=f"{league_entry.league_points} LP", inline=False)
        embed.add_field(name="승", value=league_entry.wins, inline=True)
        embed.add_field(name="패", value=league_entry.losses, inline=True)
        embed.add_field(name="승률", value=f"{league_entry.wins / (league_entry.wins + league_entry.losses) * 100:.2f}%", inline=True)
        return embed
