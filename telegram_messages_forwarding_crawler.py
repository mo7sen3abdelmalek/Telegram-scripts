#mo7sen
import asyncio
from telethon.sync import TelegramClient

api_id = #Put your api id here!
api_hash = "#Put your api hash here!"
source_channel = "#Put your source channel here!"
target_channel = "#Put your target channel here!"

client = TelegramClient("session_name", api_id, api_hash)


async def main():
    async with client:
        last_id = #Put last message id here!
        batch_size = 99 #you can edit it in range between 1 to 100 only!

        for start_id in range(1, last_id + 1, batch_size): #you can editing beginning number (1) later when you need.
            end_id = min(start_id + batch_size, last_id + 1)
            msg_ids = list(range(start_id, end_id))
            
            try:
                await client.forward_messages(target_channel, msg_ids, from_peer=source_channel)
                print(f"Forward messages from {start_id} to {end_id - 1}")
                
            except Exception as e:
                print(f"Errors were taked place when forwarding messages from {start_id} to {end_id - 1}: {e}")
            
            await asyncio.sleep(11) #edit sleeping time as you would like


with client:
    client.loop.run_until_complete(main())




