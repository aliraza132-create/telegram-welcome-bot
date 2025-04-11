from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.chat_member.new_chat_member.status == 'member':
        chat_id = update.chat_member.chat.id
        new_user = update.chat_member.new_chat_member.user.first_name
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"Welcome to the group, {new_user}! We're glad to have you here. Feel free to introduce yourself and enjoy your stay!"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

app.run_polling()