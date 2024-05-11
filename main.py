from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def henlo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Henlo!')


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('henlo', henlo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
