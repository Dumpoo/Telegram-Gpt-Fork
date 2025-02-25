import asyncio

from DeeperSeek import DeepSeek, Response

from settings import DS_USER_TOKEN, logger


class DeepSeekHandler:
    def __init__(self):
        self.api = DeepSeek(token=DS_USER_TOKEN, headless=True)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.api_init())

    async def api_init(self):
        await self.api.initialize()

    async def send_question(self, prompt: str, message: str):
        logger.info(f"def send_question - prompt: {prompt}\nmessage: {message}")
        resp = await self.api.send_message(
            message=f"{prompt}{message}",
            deepthink=True,
            search=False,
            slow_mode=True,
            slow_mode_delay=0.25,
            timeout=60,
        )
        return resp.text
