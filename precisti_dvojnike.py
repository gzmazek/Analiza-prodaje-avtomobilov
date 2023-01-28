import pandas as pd

# Ker spletna stran priljubljene avtomobile ponuja večkrat na različnih straneh, moramo pred tem podatke še počistiti
df = pd.read_csv('cars.csv')
df = df.drop_duplicates()
df.to_csv('pociscen_cars.csv', index=False)