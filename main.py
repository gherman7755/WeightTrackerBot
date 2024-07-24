from dotenv import dotenv_values
import asyncio
import telegram

config = dotenv_values(".env")
TOKEN = config["TOKEN"]

async def main():
    bot = telegram.Bot(token=TOKEN)
    async with bot:
        print(await bot.get_me())

if __name__ == "__main__":
    asyncio.run(main())