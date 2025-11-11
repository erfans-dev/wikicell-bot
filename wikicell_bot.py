from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# توکن رو از متغیر محیطی بگیر (ایمن‌تر از اینکه مستقیم بنویسی)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# تابع /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_firstname = update.effective_user.first_name
    await update.message.reply_text(f"سلام {user_firstname}! 👋\nبه WikiCell Bot خوش اومدی 🌐")

# تابع /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دستورهای موجود:\n/start - شروع بات\n/help - راهنما")

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN تنظیم نشده. لطفاً در تنظیمات Render متغیر محیطی اضافه کن.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    # ثبت دستورها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()