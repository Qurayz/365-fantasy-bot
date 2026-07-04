import pandas as pd

def get_match_players(team1, team2):
    data = [
        {"name": "Alphonso Davies", "team": "Canada", "position": "DEF", "price": 13.0, "form": 8.2},
        {"name": "Jonathan David", "team": "Canada", "position": "FWD", "price": 14.5, "form": 8.7},
        {"name": "Tajon Buchanan", "team": "Canada", "position": "MID", "price": 10.0, "form": 7.1},
        {"name": "Achraf Hakimi", "team": "Morocco", "position": "DEF", "price": 13.5, "form": 8.8},
        {"name": "Brahim Díaz", "team": "Morocco", "position": "MID", "price": 12.0, "form": 8.4},
        {"name": "Youssef En-Nesyri", "team": "Morocco", "position": "FWD", "price": 12.5, "form": 7.9},
    ]
    return pd.DataFrame(data)