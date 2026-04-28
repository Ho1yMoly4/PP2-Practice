import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

LEADERBOARD_FILE = BASE_DIR / "leaderboard.json"
SETTINGS_FILE = BASE_DIR / "settings.json"


def load_leaderboard():
    if not LEADERBOARD_FILE.exists():
        return []

    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_score(name, score, distance, coins):
    data = load_leaderboard()

    data.append({
        "name": name,
        "score": score,
        "distance": int(distance),
        "coins": coins
    })

    data.sort(key=lambda x: x["score"], reverse=True)
    data = data[:10]

    save_leaderboard(data)


def load_settings():
    if not SETTINGS_FILE.exists():
        return {
            "sound": True,
            "car_color": "blue",
            "difficulty": "normal"
        }

    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)