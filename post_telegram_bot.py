from telegram import Bot
from environs import Env


def bot_send_message(bot_token, chat_id):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text="Привет, это сообщение от бота")


def bot_send_image(bot_token, photo_path, chat_id):
    bot = Bot(token=bot_token)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption="Это картинка от бота"
        )


def main():
    env = Env()
    env.read_env()
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT_ID = env.int("CHAT_ID")
    photo_path = 'images/nasa_epic_0.png'
    bot_send_message(BOT_TOKEN, CHAT_ID)
    bot_send_image(BOT_TOKEN, photo_path, CHAT_ID)


if __name__ == "__main__":
    main()
