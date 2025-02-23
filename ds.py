import asyncio

from DeeperSeek import DeepSeek

from settings import DS_USER_TOKEN


class DeepSeekHandler:
    def __init__(self):
        self.api = DeepSeek(token=DS_USER_TOKEN, headless=True)
        asyncio.run(self.__api_init())

    async def __api_init(self):
        await self.api.initialize()

    async def send_question(self, prompt: str, message: str):
        resp = await self.api.send_message(
            message=f"{prompt}{message}",
            deepthink=True,
            search=False,
            slow_mode=True,
            slow_mode_delay=0.25,
            timeout=60,
        )
        return resp
