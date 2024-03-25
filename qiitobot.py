import telegram
from typing import Final
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
from telegram.ext import Updater
import random

TOKEN = '6715143051:AAGXK_YtbWJqQ8ekoQ5o_O_ZEMK8UEYyur8'
BOT_USERNAME: Final = '@Qiitobot'  # Renamed the bot to Qiitobot

# Dictionary of responses
responses = {
    'greetings': ["Hey there!", "Hello!", "Hi!"],
    'positive': ["That's awesome!", "Glad to hear that!"],
    'negative': ["I'm sorry to hear that.", "Hope things get better soon."],
    'python': ['Remember to subscribe!']
}

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am Qiitobot!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am Qiitobot! Here are some available commands:\n'
                                    '/start - Start the conversation\n'
                                    '/help - Get help\n'
                                    '/custom - Trigger a custom command\n'
                                    '/info - Get information about Qiitobot')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!') 

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Qiitobot is a simple bot developed by Qiita for providing assistance and fun interactions.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text.lower()  # Convert text to lowercase for easier processing
    print(f'User ({update.message.chat.id}) in ({message_type}): "{text}"')

    # Check for specific keywords in the user's message and respond accordingly
    if 'hello' in text or 'hi' in text or 'hey' in text:
        response = random.choice(responses['greetings'])
    elif any(pos_word in text for pos_word in ['great', 'good', 'awesome', 'fantastic']):
        response = random.choice(responses['positive'])
    elif any(neg_word in text for neg_word in ['bad', 'not good', 'terrible']):
        response = random.choice(responses['negative'])
    elif 'i love python' in text:
        response = random.choice(responses['python'])
    else:
        response = random.choice(["I'm not sure I understand.", "Could you please rephrase that?"])

    print('Qiitobot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    if name == 'main':
        print('Starting bot...')

app = Application.builder().token(TOKEN).build()

# Commands
app.add_handler(CommandHandler('start', start_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('custom', custom_command))
app.add_handler(CommandHandler('info', info_command))

# Messages
app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Errors
app.add_error_handler(error)

# Polls the bot
print("Polling...")
app.run_polling(poll_interval=3)
