import pandas as pd

calories = {'Day 1:': 1000, 'Day 2': 2000, 'Day 3': 3000, 'Day 4': 4000}

calorieSeries = pd.Series(calories)
calorieSeries.loc['Day 3'] += 500
print(calorieSeries)