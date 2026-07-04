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
        "⚽ **Bet365 Fantasy Bot**\n\n"
        "Send any match like:\n"
        "`Canada vs Morocco`\n"
        "`France vs Brazil`\n"
        "`Argentina vs Spain`\n\n"
        "I'll suggest the best 6 players!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    await update.message.reply_text(f"🔍 Analyzing **{text}**...")
    
    try:
        df = get_match_players(text)
        df = enhance_projections(df)
        best = optimize_lineup(df, budget=70, num_players=6)
        
        total = round(best['xfp'].sum(), 1)
        
        response = f"🏆 **Best Fantasy Lineup for {text}**\n\n"
        response += f"**Projected Points: {total}**\n\n"
        
        for _, p in best.iterrows():
            response += f"• **{p['name']}** ({p['team']}) — {p['position']} | 💰 {p['price']}M | ⭐ {p['xfp']}\n"
        
        response += "\n💡 These are high-value picks to help top the leaderboard!"
        await update.message.reply_text(response, parse_mode='Markdown')
        
    except Exception as e:
        await update.message.reply_text("Sorry, something went wrong. Try another match like 'Canada vs Morocco'.")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Bot is running on the cloud...")
    app.run_polling()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
