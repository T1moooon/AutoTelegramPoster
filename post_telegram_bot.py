import os
import random
import argparse
from telegram import Bot
from dotenv import load_dotenv


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
    load_dotenv()
    bot_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
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
    bot_send_image(bot_token, photo_path, chat_id)


if __name__ == "__main__":
    main()
