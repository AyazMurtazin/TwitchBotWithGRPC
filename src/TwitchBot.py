from twitchio.ext import commands
import os
import asyncio
import sys
import redis

from dotenv import load_dotenv
load_dotenv()

# Access environment variables
TMI_TOKEN = os.getenv('TMI_TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
BOT_NICK = os.getenv('BOT_NICK')
BOT_PREFIX = os.getenv('BOT_PREFIX')
try:
    CHANNEL = sys.argv[1]
except:
    print("No channel provided")

def vars2(x):
    if hasattr(x, '__dict__'):
        return vars(x)
    else:
        ret = {slot: getattr(x, slot) for slot in x.__slots__}
        for cls in type(x).mro():
            spr = super(cls, x)
            if not hasattr(spr, '__slots__'):
                break
            for slot in spr.__slots__:
                ret[slot] = getattr(x, slot)
        return ret


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TMI_TOKEN,
            client_id=CLIENT_ID,
            nick=BOT_NICK,
            prefix=BOT_PREFIX,
            initial_channels=[CHANNEL])
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
        self.channel_name = CHANNEL

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.author.name != self.nick and not message.echo:
            # print(message.content)
            await self.handle_message(message.content)

    async def handle_message(self, message):
        # Push message to Redis message queue
        self.redis_client.rpush(self.channel_name, message)

    


if __name__ == "__main__":
    bot = Bot()
    bot.run()
