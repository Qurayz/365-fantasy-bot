from pulp import *

def optimize_lineup(df, budget=65, num_players=6):
    prob = LpProblem("Lineup", LpMaximize)
    select = LpVariable.dicts("select", df.index, cat="Binary")
    
    prob += lpSum(select[i] * df.loc[i,'xfp'] for i in df.index)
    prob += lpSum(select[i] * df.loc[i,'price'] for i in df.index) <= budget
    prob += lpSum(select[i] for i in df.index) == num_players
    
    prob.solve(PULP_CBC_CMD(msg=0))
    
    selected = df.loc[[i for i in df.index if select[i].value() == 1]]
    return selected