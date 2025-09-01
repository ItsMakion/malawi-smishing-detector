from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from detector.rule_based import is_smishing
from detector.ml_classifier import predict_message

# Replace with your bot token
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to the Malawi Smishing Detector bot.\nSend any message and I will tell you if it looks suspicious."
    )

def handle_message(update: Update, context: CallbackContext):
    msg = update.message.text
    rule_flag = is_smishing(msg)
    ml_flag = predict_message(msg)
    if rule_flag or ml_flag == "smishing":
        response = "⚠️ Likely smishing! Be careful."
    else:
        response = "✅ Looks safe."
    update.message.reply_text(response)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("Bot started. Press Ctrl+C to stop.")
    updater.idle()

if __name__ == "__main__":
    main()
