import os
import random
import time
import argparse
from telegram import Bot
from dotenv import load_dotenv


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
    load_dotenv()
    BOT_TOKEN = os.environ['TG_BOT_TOKEN']
    DELAY = int(os.getenv("TG_BOT_DELAY", "4")) * 3600
    CHAT_ID = os.environ['TG_CHAT_ID']
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
