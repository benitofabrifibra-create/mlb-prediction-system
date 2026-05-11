from fastapi import FastAPI
from data_fetcher import get_mlb_schedule, get_weather, get_latest_news
from agents import analyze
from predict import score
from config import MIN_CONF
app = FastAPI()
@app.get("/predict")
def run():
    games = get_mlb_schedule()
    if not games: return {"msg": "📅 Nessuna partita MLB oggi."}
    news = get_latest_news()
    for g in games:
        w = get_weather(g["venue_coords"][0], g["venue_coords"][1])
        dir, ai_conf, why = analyze(g, w, news)
        ml_pick, ml_conf = score(g)
        final_conf = round((ai_conf + ml_conf) / 2, 2)
        if final_conf >= MIN_CONF:
            return {
                "match": f"{g['away']} @ {g['home']}", "venue": g["venue_name"], "umpire": g["umpire_home"],
                "weather": w, "pick": ml_pick if ml_conf > ai_conf else dir, "line": 8.5, "confidence": final_conf,
                "reason": why
            }
    return {"msg": "🟡 Confidence bassa oggi. Nessuna pick consigliata."}
