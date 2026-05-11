import joblib, pandas as pd
from config import MODEL_PATH
model = joblib.load(MODEL_PATH)
def score(game):
    feats = pd.DataFrame([{"pitcher_diff": 0.1, "venue_factor": 100, "wind_impact": 0.5, "umpire_bias": 0.0, "news_sentiment": 0.5}])
    prob = model.predict_proba(feats)[0][1]
    conf = abs(prob - 0.5) * 2
    pick = "Over" if prob > 0.5 else "Under"
    return pick, round(conf, 2)
