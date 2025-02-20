import os
import random
import argparse
from telegram import Bot
from environs import Env


def bot_send_image(bot_token, photo_path, chat_id):
    bot = Bot(token=bot_token)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo,
        )


def get_random_image(image_dir):
    images = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        raise FileNotFoundError("В директории нет изображений.")
    return random.choice(images)


def main():
    env = Env()
    env.read_env()
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT_ID = env.int("CHAT_ID")
    parser = argparse.ArgumentParser(description="Отправка сообщений и изображений в Telegram-канал.")
    parser.add_argument(
        "--image",
        type=str,
        help="Путь к изображению для отправки. Если не указан, выбирается случайное изображение из директории images.",
        default=None
    )
    args = parser.parse_args()
    if args.image:
        photo_path = args.image
    else:
        try:
            photo_path = get_random_image("images")
        except FileNotFoundError as e:
            print(e)
            return
    bot_send_image(BOT_TOKEN, photo_path, CHAT_ID)


if __name__ == "__main__":
    main()
