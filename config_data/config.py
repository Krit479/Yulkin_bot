from dataclasses import dataclass

#from environs import Env
import os


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    #env = Env()
    #env.read_env(path)
    return Config(tg_bot=TgBot(
                    token=os.getenv('BOT_TOKEN'),
        			admin_ids=os.getenv('ADMIN_IDS')))
                    #admin_ids=list(map(int, os.getenv('ADMIN_IDS')))))
