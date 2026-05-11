import os, requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TG_TOKEN
URL = os.getenv("BACKEND_URL", "http://localhost:8000")
async def predict(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Analisi live...")
    try:
        r = requests.get(f"{URL}/predict", timeout=20).json()
        if "msg" in r: await update.message.reply_text(r["msg"])
        else:
            txt = f"⚾ Match: {r['match']}\n🏟️ {r['venue']} | 🕵️ {r['umpire']}\n🌦️ {r['weather']}\n📊 Pick: {r['pick']} Total\n📏 Linea: {r['line']}\n🔍 Conf: {r['confidence']}\n🤖 {r['reason']}"
            await update.message.reply_text(txt)
    except Exception as e: await update.message.reply_text(f"❌ Errore: {str(e)}")
def main():
    app = Application.builder().token(TG_TOKEN).build()
    app.add_handler(CommandHandler("predict", predict))
    app.run_polling()
if __name__ == "__main__": main()
