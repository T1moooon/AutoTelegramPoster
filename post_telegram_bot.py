from telegram import Bot
from environs import Env


def bot_send_message(bot_token, chat_id):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text="Привет, это сообщение от бота")


def main():
    env = Env()
    env.read_env()
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT_ID = env.int("CHAT_ID")
    bot_send_message(BOT_TOKEN, CHAT_ID)


if __name__ == "__main__":
    main()
