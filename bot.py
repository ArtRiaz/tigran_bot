import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

from tgbot.config import load_config, Config
from tgbot.handlers import routers_list
from tgbot.middlewares.config import ConfigMiddleware
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

dp = Dispatcher()


def register_global_middlewares(dp: Dispatcher, config: Config):
    middleware_types = [
        ConfigMiddleware(config),
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


async def on_startup(bot: Bot, config: Config):
    allowed_updates = dp.resolve_used_update_types()
    await bot.set_webhook(f"{config.webhook.webhook_url}{config.webhook.webhook_path}", allowed_updates=allowed_updates)


def setup_logging():
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


def get_storage(config):
    """
    Return storage based on the provided configuration.

    Args:
        config (Config): The configuration object.

    Returns:
        Storage: The storage object based on the configuration.

    """
    if config.tg_bot.use_redis:
        return RedisStorage.from_url(
            config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
    else:
        return MemoryStorage()


def main() -> None:
    setup_logging()

    config = load_config(".env")
    storage = get_storage(config)

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(storage=storage)

    register_global_middlewares(dp, config)

    dp.include_routers(*routers_list)  # Include all_states

    requests_handler = SimpleRequestHandler(dp, bot,
                                            )

    app = web.Application()

    requests_handler.register(app, path=config.webhook.webhook_path)

    dp.startup.register(on_startup)
    setup_application(app, dp, bot=bot, config=config)
    web.run_app(app, host=config.webhook.webapp_host, port=config.webhook.webapp_port)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
