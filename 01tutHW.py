import pandas as pd

events = {'China Silk Road': -2000, 'Greece Formation:': -700, 'Roman Empire Collapse': 472, 'World War I': 1945}

eventSeries = pd.Series(events)
silkRoadTime = eventSeries.loc['China Silk Road']
eventSeries.loc['World War I'] = 1914




print(eventSeries)
print('___________________________\n')
print(f"China Silk Road happened in the year: {silkRoadTime}")
print('___________________________\n')
print(f'Instead of 1945, ww1 happened in the year: {eventSeries.loc['World War I']}')
