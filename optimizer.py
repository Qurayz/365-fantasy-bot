from pulp import *

def optimize_lineup(df, budget=70, num_players=6):
    """Select best lineup under budget"""
    if len(df) < num_players:
        return df.head(num_players)
    
    prob = LpProblem("Fantasy_Lineup", LpMaximize)
    select = LpVariable.dicts("select", df.index, cat="Binary")
    
    # Maximize expected points
    prob += lpSum(select[i] * df.loc[i, 'xfp'] for i in df.index)
    
    # Budget constraint
    prob += lpSum(select[i] * df.loc[i, 'price'] for i in df.index) <= budget
    
    # Exactly 6 players
    prob += lpSum(select[i] for i in df.index) == num_players
    
    # Max 3 per team
    for team in df['team'].unique():
        team_idx = df[df['team'] == team].index
        prob += lpSum(select[i] for i in team_idx) <= 3
    
    prob.solve(PULP_CBC_CMD(msg=0))
    
    selected = df.loc[[i for i in df.index if select[i].value() == 1]]
    return selected
