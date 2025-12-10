import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    await update.message.reply_text("🎬 Salom! Kino bot ishlaydi.\nRaqam yozing: 123")

async def echo(update: Update, context):
    text = update.message.text
    if text.isdigit():
        await update.message.reply_text(f"✅ {text} kod qabul qilindi!")
    else:
        await update.message.reply_text("❌ Faqat raqam yozing!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == '__main__':
    main()
