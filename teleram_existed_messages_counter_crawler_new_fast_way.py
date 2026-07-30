#mo7sen
import asyncio
from telethon import TelegramClient

api_id = #Put your api id here!
api_hash = "#Put your api hash here!"
source_channel = "#Put your source channel here!"

client = TelegramClient("session_name", api_id, api_hash)


async def main():
    count = 0

    async with client:
        async for msg in client.iter_messages(source_channel, reverse=True):
            count += 1

            if count % 1000 == 0:
                print(f"Counted {count} messages...")


    print("=" * 40)
    print(f"Total existed messages number: {count}")
    print("=" * 40)


if __name__ == "__main__":
    asyncio.run(main())




