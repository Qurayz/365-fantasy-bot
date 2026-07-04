import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

from data_fetcher import get_match_players
from projections import enhance_projections
from optimizer import optimize_lineup

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ **Fantasy Bot Ready!**\n\n"
        "Send a match like:\n"
        "Canada vs Morocco"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    await update.message.reply_text(f"Analyzing {text}...")
    
    try:
        df = get_match_players(text, text)
        df = enhance_projections(df)
        best = optimize_lineup(df)
        
        response = f"**Best Lineup for {text}**\n\n"
        response += f"Projected Points: {round(best['xfp'].sum(),1)}\n\n"
        
        for _, p in best.iterrows():
            response += f"• {p['name']} ({p['team']}) - {p['position']} | {p['price']}M | {p['xfp']}pts\n"
        
        await update.message.reply_text(response, parse_mode='Markdown')
    except:
        await update.message.reply_text("Sorry, something went wrong.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()