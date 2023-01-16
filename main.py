import functions_framework
import os
import telegram
from telegram import Update
from telegram.ext import Application, Updater,Dispatcher, CommandHandler, MessageHandler, Filters,  ContextTypes
# Import logging module
import logging
import sys
# Define a function for the /start command
async def start(update: Update, context: ContextTypes) -> None:
   # Get chat_id from update
   chat_id = update.message.chat.id
   # Welcome message
   message = 'Welcome to my bot!'
   # Send message to chat_id
   await update.message.reply_text(message)
   


   
# Get TOKEN from environment variable
TOKEN = os.environ.get('TOKEN')

# Create the Application and pass it your bot's token.
app = Application.builder().token(TOKEN).build()
@functions_framework.http
def main(request):
   # Check if request is POST
   if request.method == 'POST':
      # Create a dispatcher instance
      
      # Get update from request
      update = Update.de_json(request.get_json(force=True), app.bot)
      # send message to log
      logging.info(f'Update: hello')
      # Add handlers
      app.add_handler(CommandHandler('start', start))
      # Add handlers for echo
      
      app.process_update(update) 
      return {'ok':TOKEN}

   
   return f'TOKEN: {TOKEN}!'
