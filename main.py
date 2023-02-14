from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from comandbot import *


app = ApplicationBuilder().token("your token").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", helpbot))

app.run_polling()