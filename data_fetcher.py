import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")

def get_match_players(match_query):
    """Dynamic - tries to get real players from the two teams"""
    headers = {'x-apisports-key': API_KEY} if API_KEY else {}
    
    # Simple team name mapping (expand as needed)
    team_map = {
        "canada": 109,
        "morocco": 31,
        "france": 2,
        "brazil": 6,
        "argentina": 9,
        "spain": 5,
        "germany": 3,
        "england": 1,
    }
    
    # Try to extract two teams
    words = match_query.lower().replace("vs", " ").split()
    team1 = next((w for w in words if w in team_map), "canada")
    team2 = next((w for w in reversed(words) if w in team_map and w != team1), "morocco")
    
    all_players = []
    
    for team_name, team_id in [(team1, team_map.get(team1)), (team2, team_map.get(team2))]:
        if not team_id:
            continue
        try:
            resp = requests.get(f"https://v3.football.api-sports.io/players?team={team_id}&season=2025", 
                              headers=headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json().get('response', [])
                for item in data[:15]:  # limit to top 15 per team
                    p = item['player']
                    all_players.append({
                        "name": p['name'],
                        "team": team_name.title(),
                        "position": p.get('position', 'MID')[:3].upper(),
                        "price": round(8 + (p.get('age', 25) % 7), 1),
                        "form": round(6 + (p.get('age', 25) % 4), 1)
                    })
        except:
            pass  # fallback if API fails
    
    if not all_players:
        # Fallback pool
        all_players = [
            {"name": "Alphonso Davies", "team": "Canada", "position": "DEF", "price": 13.5, "form": 8.5},
            {"name": "Achraf Hakimi", "team": "Morocco", "position": "DEF", "price": 13.8, "form": 8.9},
            {"name": "Kylian Mbappé", "team": "France", "position": "FWD", "price": 15.5, "form": 9.2},
        ]
    
    df = pd.DataFrame(all_players)
    return df
