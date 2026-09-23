# bot.py — Python 3.11, pip install python-telegram-bot==21.6
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8732154500:AAHqiXtcJseysDbuVlC9J8j-rGu1g-_x920"
CHAT_ID = "8099108408"

async def on_photo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    f = await ctx.bot.get_file(photo.file_id)
    path = f"capture_{update.message.message_id}.jpg"
    await f.download_to_drive(path)
    print(f"[+] saved {path}")

async def on_doc(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    d = update.message.document
    f = await ctx.bot.get_file(d.file_id)
    path = f"capture_{update.message.message_id}_{d.file_name}"
    await f.download_to_drive(path)
    print(f"[+] saved {path}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, on_photo))
    app.add_handler(MessageHandler(filters.Document.IMAGE, on_doc))
    print("[*] bot up")
    app.run_polling()

if __name__ == "__main__":
    main()