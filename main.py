from telegram.ext import Updater, CommandHandler

# Start Command Handler
def start(update, context):
    user = update.effective_user
    update.message.reply_text(f"Welcome {user.first_name} to M8N-Dating Bot! Please use the commands to proceed.")

# Main Function to Configure and Run Bot
def main():
    # Load Bot Token
    TOKEN = "your-telegram-bot-token-here"

    # Set up the Updater and Dispatcher
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # Add Handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Start Bot
    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
