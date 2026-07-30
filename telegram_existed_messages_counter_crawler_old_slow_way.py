#mo7sen
import asyncio
from telethon import TelegramClient

api_id = #Put your api id here!
api_hash = "#Put your api hash here!"
source_channel = "#Put your source channel here!"

client = TelegramClient("session_name", api_id, api_hash)


async def main():
    async with client:
        last_id = #Put last message id here!
        batch_size = 99
        count = 0

        for start_id in range(1, last_id + 1, batch_size):
            end_id = min(start_id + batch_size, last_id + 1)
            msg_ids = list(range(start_id, end_id))

            messages = await client.get_messages(
                source_channel,
                ids=msg_ids
            )

            for msg in messages:
                if msg is None:
                    continue

                count += 1

            print(f"Messages were scanned from {start_id} to {end_id - 1} | The count now is: {count}")
            await asyncio.sleep(11) #edit sleep counter as you would like


        print("=" * 40)
        print(f"Total existed messages number: {count}")
        print("=" * 40)


with client:
    client.loop.run_until_complete(main())




