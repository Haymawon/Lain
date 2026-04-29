import logging
from telegram import Update
from telegram.ext import ContextTypes
from app.config import ADMIN_CHAT_ID

logger = logging.getLogger(__name__)

async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = user.full_name
    user_id = user.id
    username = f"@{user.username}" if user.username else "no username"
    message = update.message

    await message.reply_text("I will hit you back as soon as possible")

    if message.photo:
        media_type = "📷 Photo"
        caption = message.caption or ""
    elif message.video:
        media_type = "🎬 Video"
        caption = message.caption or ""
    elif message.document:
        media_type = "📎 Document"
        caption = message.caption or ""
    elif message.audio:
        media_type = "🎵 Audio"
        caption = message.caption or ""
    elif message.voice:
        media_type = "🎤 Voice message"
        caption = message.caption or ""
    elif message.video_note:
        media_type = "🟣 Video note"
        caption = ""
    elif message.sticker:
        media_type = "⭐ Sticker"
        caption = message.sticker.emoji or ""
    elif message.animation:
        media_type = "🎞️ GIF / Animation"
        caption = message.caption or ""
    elif message.text:
        media_type = "💬 Text"
        caption = message.text
    else:
        media_type = "❓ Other message type"
        caption = ""

    notification = (
        f"📩 New message from {user_name} ({username}, ID: {user_id})\n"
        f"Type: {media_type}"
    )
    if caption:
        notification += f"\nCaption/Text: {caption}"

    try:
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=notification)
        await message.forward(chat_id=ADMIN_CHAT_ID)
    except Exception as e:
        logger.error(f"Failed to forward to admin: {e}")