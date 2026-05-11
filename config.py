import os
from dotenv import load_dotenv
load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")
TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MODEL_PATH = "models/mlb_xgb.pkl"
MIN_CONF = 0.62
DB_PATH = "data/tracker.db"
