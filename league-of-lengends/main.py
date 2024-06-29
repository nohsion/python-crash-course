from lol_manager import LolManager
from discord_bot import DiscordBot


if __name__ == '__main__':
    bot = DiscordBot(LolManager())
    bot.run()
