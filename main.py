from telegram import Update, WebAppInfo, MenuButtonWebApp, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

# --- CONFIGURATION ---
# 1. PASTE YOUR BOT TOKEN HERE
BOT_TOKEN = "8123604231:AAFUIQCXc9meiQlA56veQjaiNs18H6ieuVk" 

# 2. PASTE YOUR NETLIFY WEB APP URL HERE
WEB_APP_URL = "https://virtualv1.vercel.app/"
# ---------------------

# This command handler is triggered when a user types /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Sends a welcome message and sets up the menu button to launch the web app.
    """
    # Set up the Menu Button to show the "HaldarAi" app
    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(text="Launch App", web_app=WebAppInfo(url=WEB_APP_URL))
    )
    
    # Also, send a welcome message with a keyboard button as another way to open the app
    keyboard = [
        [KeyboardButton("🚀 Launch Virtual v1", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    
    await update.message.reply_text(
        "Welcome to Virtual v1! 🎉\n\n"
        "Click the 'Launch' button below or use the menu to open the app.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

def main() -> None:
    """Start the bot."""
    print("Starting bot...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is running! Go to Telegram and press /start.")
    application.run_polling()

if __name__ == "__main__":
    main()