from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"👋 Hi {user.full_name}!\n"
        "Send me any message – text, photo, video, etc. – and I'll forward it "
        "to the admin. You'll get an automatic reply right away."
    )
    await update.message.reply_text(welcome_text)