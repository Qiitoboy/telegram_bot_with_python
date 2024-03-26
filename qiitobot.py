

import telegram
from typing import Final
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
from telegram.ext import Updater
import random

TOKEN = '6715143051:AAGXK_YtbWJqQ8ekoQ5o_O_ZEMK8UEYyur8'

# Dictionary of movies by genre
movies = {
    'comedy': ['The Hangover', 'Superbad', 'Anchorman', 'Dumb and Dumber', 'Bridesmaids',
               'Airplane!', 'Monty Python and the Holy Grail', 'Groundhog Day', 'Napoleon Dynamite',
               'The Big Lebowski', 'Shaun of the Dead', 'Hot Fuzz', 'Mean Girls', 'Wedding Crashers',
               'Pitch Perfect', 'Step Brothers', 'Zoolander', 'Ted', 'Crazy Rich Asians', 'The 40-Year-Old Virgin',
               'Office Space', 'Super Troopers', 'Austin Powers: International Man of Mystery'],
    'action': ['The Dark Knight', 'Inception', 'The Matrix', 'Die Hard', 'Mad Max: Fury Road',
               'Gladiator', 'Terminator 2: Judgment Day', 'Braveheart', 'The Bourne Identity', '300',
               'Jurassic Park', 'Avatar', 'Indiana Jones and the Raiders of the Lost Ark', 'Mission: Impossible',
               'The Avengers', 'Fast & Furious', 'Kill Bill: Vol. 1', 'John Wick', 'Black Panther', 'Spider-Man: Homecoming',
               'Captain America: The Winter Soldier', 'The Terminator', 'The Incredibles'],
    'drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Pulp Fiction', 'Schindler\'s List',
              'Goodfellas', 'Fight Club', 'The Departed', 'The Green Mile', 'American History X',
              'Saving Private Ryan', 'The Prestige', 'American Beauty', 'A Beautiful Mind', 'Rain Man',
              'The Silence of the Lambs', 'The Truman Show', 'A Few Good Men', 'The Pursuit of Happyness',
              'The Revenant', 'The Social Network', 'Dallas Buyers Club', 'Shutter Island'],
    'romance': ['Titanic', 'The Notebook', 'Pride and Prejudice', 'La La Land', 'Romeo + Juliet',
                'Dirty Dancing', 'The Fault in Our Stars', 'The Princess Bride', 'A Star is Born', 'Notting Hill',
                '10 Things I Hate About You', 'Eternal Sunshine of the Spotless Mind', 'Crazy, Stupid, Love',
                'The Shape of Water', 'Before Sunrise', '500 Days of Summer', 'Ghost', 'Love Actually',
                'About Time', 'Serendipity', 'The Time Traveler\'s Wife', 'Amélie', 'When Harry Met Sally...'],
    'sci-fi': ['Interstellar', 'Star Wars: A New Hope', 'Blade Runner', 'The Martian', 'Avatar',
               'The Matrix', 'Inception', 'Jurassic Park', 'Terminator 2: Judgment Day', 'Alien',
               'Back to the Future', 'The Fifth Element', 'E.T. the Extra-Terrestrial', 'The Terminator',
               'The Empire Strikes Back', 'The Day the Earth Stood Still', 'Close Encounters of the Third Kind',
               'War for the Planet of the Apes', 'Gravity', 'District 9', 'The War of the Worlds', 'Ex Machina',
               '2001: A Space Odyssey'],
    'horror': ['The Shining', 'Psycho', 'Get Out', 'A Nightmare on Elm Street', 'The Exorcist',
               'Halloween', 'The Conjuring', 'The Silence of the Lambs', 'The Texas Chain Saw Massacre',
               'Night of the Living Dead', 'The Blair Witch Project', 'Poltergeist', 'Scream', 'Hereditary',
               'Paranormal Activity', 'It', 'Rosemary\'s Baby', 'The Ring', 'The Babadook', 'The Sixth Sense',
               'Insidious', 'Annabelle', 'The Descent', 'Sinister']
}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = ("Hello! I'm Qiito, a movie Suggester bot.\n"
                "You can ask me to suggest a movie based on its genre.\n"
                "To get started, type '/suggest_movie <genre>'.\n"
                "For example, '/suggest_movie comedy' will suggest a comedy movie.")
    await update.message.reply_text(response)

async def suggest_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract the genre mentioned by the user
    text = update.message.text.lower()
    parts = text.split()
    if len(parts) != 2:
        await update.message.reply_text('Invalid command format. Please use: /suggest_movie <genre>')
        return
    genre = parts[1]
    if genre in movies:
        suggested_movie = random.choice(movies[genre])
        await update.message.reply_text(f'Try watching "{suggested_movie}"?')
    else:
        await update.message.reply_text(f'Sorry, I couldn\'t find any movies in the "{genre}" genre.')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

app = Application.builder().token(TOKEN).build()

# Commands
app.add_handler(CommandHandler('start', start_command))
app.add_handler(CommandHandler('suggest_movie', suggest_movie_command))

# Errors
app.add_error_handler(error)

# Polls the bot
print("Polling...")
app.run_polling(poll_interval=3)
