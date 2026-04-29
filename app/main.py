import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from app.config import BOT_TOKEN
from app.handlers.start import start
from app.handlers.messages import handle_all_messages

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(~filters.COMMAND, handle_all_messages))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()