from langchain_groq import ChatGroq
from config import GROQ_KEY
llm = ChatGroq(model="llama-3-70b-8192", temperature=0.05, groq_api_key=GROQ_KEY)
def analyze(game, weather, news):
    prompt = f"""Analista MLB. Match: {game['away']} @ {game['home']} | Pitcher: {game['ap']} vs {game['hp']} | Umpire: {game['umpire_home']} | Meteo: {weather} | News: {news}
    Analizza trappole di mercato, fatica, park factor, umpire tendency.
    Rispondi SOLO così:
    Direzione: Over/Under
    Confidence: 0.50-0.85
    Motivo: max 15 parole."""
    txt = llm.invoke(prompt).content.strip()
    dir = txt.split("Direzione: ")[1].split("\n")[0]
    conf = float(txt.split("Confidence: ")[1].split("\n")[0])
    why = txt.split("Motivo: ")[1]
    return dir, conf, why
