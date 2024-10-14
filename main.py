import os

import dotenv
import validators
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

dotenv.load_dotenv()


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    if validators.url(message):
        await update.message.reply_text("It's a link!")
    else:
        await update.message.reply_text(message)


def main() -> None:
    application = Application.builder().token(os.environ.get('BOT_TOKEN')).build()
    # application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
