import requests, feedparser
from datetime import date
def get_mlb_schedule():
    today = date.today().isoformat()
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}"
    res = requests.get(url, timeout=10).json()
    games = []
    for d in res.get("dates", []):
        for g in d.get("games", []):
            if g["status"]["abstractGameState"] == "Preview":
                t = g["teams"]
                games.append({
                    "pk": g["gamePk"],
                    "away": t["away"]["team"]["name"],
                    "home": t["home"]["team"]["name"],
                    "ap": t["away"].get("probablePitcher", {}).get("fullName", "TBD"),
                    "hp": t["home"].get("probablePitcher", {}).get("fullName", "TBD"),
                    "venue_name": g["venue"]["name"],
                    "venue_coords": (g["venue"].get("location", {}).get("latitude", 0), g["venue"].get("location", {}).get("longitude", 0)),
                    "umpire_home": g.get("officials", [{}])[0].get("official", {}).get("fullName", "Unknown")
                })
    return games
def get_weather(lat, lon):
    if lat == 0: return "Dati meteo non disponibili"
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&windspeed_unit=mph&temperature_unit=f"
    try:
        w = requests.get(url, timeout=5).json().get("current_weather", {})
        return f"{w['temperature']}°F, vento {w['windspeed']}mph"
    except: return "Meteo N/D"
def get_latest_news():
    feed = feedparser.parse("https://www.mlb.com/feeds/rss/news.xml")
    headlines = [entry.title for entry in feed.entries[:3]]
    return " | ".join(headlines) if headlines else "Nessuna news"
