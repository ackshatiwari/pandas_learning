import pandas as pd

# filtering

df = pd.read_csv("data.csv")

usa_users = df[df['country'] == 'USA']

young_users = df[df['age'] <= 25]

old_users = df[df['age'] > 40]

middle_age_users = df[(df['age'] > 25) & (df['age'] < 40)]

active_or_old_users = df[(df['age'] > 40) | (df['is_active'])]

print(middle_age_users)