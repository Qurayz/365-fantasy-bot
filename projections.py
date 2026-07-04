def calculate_xfp(row):
    return round(row['form'] * 1.2, 1)

def enhance_projections(df):
    df['xfp'] = df.apply(calculate_xfp, axis=1)
    return df