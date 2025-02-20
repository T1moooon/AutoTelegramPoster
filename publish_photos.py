import os
import random
import time
import argparse
from telegram import Bot
from environs import Env


def publish_photos(bot_token, folder, chat_id, delay):
    bot = Bot(token=bot_token)
    photos = [os.path.join(folder, photo) for photo in os.listdir(folder)]
    if not photos:
        print("В директории нет фотографий.")
        return
    while True:
        random.shuffle(photos)
        for photo in photos:
            with open(photo, 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            print(f"Опубликовано: {photo}")
            time.sleep(delay)


def main():
    env = Env()
    env.read_env()
    BOT_TOKEN = env.str("BOT_TOKEN")
    DELAY = env.int("DELAY", 4) * 3600
    CHAT_ID = env.int("CHAT_ID")
    parser = argparse.ArgumentParser(description="Публикация фотографий в Telegram-канал.")
    parser.add_argument(
        "--folder",
        default="images",
        help="Папка с фотографиями для публикации."
    )
    args = parser.parse_args()
    publish_photos(BOT_TOKEN, args.folder, CHAT_ID, DELAY)


if __name__ == "__main__":
    main()
