import pandas as pd

def get_match_players(match_query):
    """Realistic player data for multiple matches"""
    
    # Expanded real player pool (World Cup focus)
    players = [
        # Canada
        {"name": "Alphonso Davies", "team": "Canada", "position": "DEF", "price": 13.5, "form": 8.5},
        {"name": "Jonathan David", "team": "Canada", "position": "FWD", "price": 14.8, "form": 8.9},
        {"name": "Tajon Buchanan", "team": "Canada", "position": "MID", "price": 10.5, "form": 7.4},
        {"name": "Dayne St. Clair", "team": "Canada", "position": "GK", "price": 8.0, "form": 6.8},
        {"name": "Junior Hoilett", "team": "Canada", "position": "MID", "price": 9.0, "form": 6.5},
        
        # Morocco
        {"name": "Achraf Hakimi", "team": "Morocco", "position": "DEF", "price": 13.8, "form": 8.9},
        {"name": "Brahim Díaz", "team": "Morocco", "position": "MID", "price": 12.5, "form": 8.6},
        {"name": "Youssef En-Nesyri", "team": "Morocco", "position": "FWD", "price": 12.8, "form": 8.2},
        {"name": "Hakim Ziyech", "team": "Morocco", "position": "MID", "price": 11.5, "form": 7.8},
        {"name": "Sofyan Amrabat", "team": "Morocco", "position": "MID", "price": 10.0, "form": 7.3},
        
        # Other common teams for testing
        {"name": "Kylian Mbappé", "team": "France", "position": "FWD", "price": 15.5, "form": 9.2},
        {"name": "Lionel Messi", "team": "Argentina", "position": "FWD", "price": 14.0, "form": 8.7},
        {"name": "Vinicius Jr", "team": "Brazil", "position": "FWD", "price": 14.2, "form": 8.8},
    ]
    
    df = pd.DataFrame(players)
    return df
