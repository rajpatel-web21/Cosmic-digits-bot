import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TELEGRAM_TOKEN")

def reduce_to_single_digit(number):
    while number > 9:
        number = sum(int(d) for d in str(number))
    return number

def calculate_life_path(dob):
    digits = [int(d) for d in dob if d.isdigit()]
    return reduce_to_single_digit(sum(digits))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Welcome to Cosmic Digits 🔮\n\n"
        "Please enter your date of birth in DDMMYYYY format.\n"
        "Example: 15081990"
    )

async def handle_dob(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text.isdigit() or len(text) != 8:
        await update.message.reply_text("❌ Please enter DOB in DDMMYYYY format.")
        return

    life_path = calculate_life_path(text)

    await update.message.reply_text(
        f"✨ Your Life Path Number is {life_path} ✨\n\n"
        "This is your FREE basic reading.\n\n"
        "Type /premium to unlock the full report."
    )

async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 PREMIUM REPORT\n\n"
        "Unlock your full numerology report for £4.\n\n"
        "Payment link coming soon."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("premium", premium))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_dob))

    app.run_polling()

if __name__ == "__main__":
    main()
