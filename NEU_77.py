import pandas as pd

#https://www.football-data.co.uk/data.php

data = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')

#https://www.football-data.co.uk/mmz4281/2425/E0.csv
#https://www.football-data.co.uk/mmz4281/2425/E1.csv
#https://www.football-data.co.uk/mmz4281/2425/E2.csv
#https://www.football-data.co.uk/mmz4281/2425/E3.csv
#https://www.football-data.co.uk/mmz4281/2425/EC.csv

#print(data)


data.rename(columns = {'FTHG': 'home_goals',
                       'FTAG': 'away_goals'}, inplace = True)

print(data.iloc[:10,0:7])

print('https://www.football-data.co.uk/mmz4281/' +'2425' + '/' + 'E0' + '.csv')

root = 'https://www.football-data.co.uk/mmz4281/'

leagues2 = ['E0', 'E1', 'E2', 'E3', 'EC']

leagues = [f'E{i}' for i in range(0, 4)] + ['EC']
print(leagues)

for league in leagues2:
    print(f'https://www.football-data.co.uk/mmz4281/2425/{league}.csv')




data_all = []
for league in leagues2:
    df = pd.read_csv(f'https://www.football-data.co.uk/mmz4281/2425/{league}.csv')
    data_all.append(df)

print(data_all[0].iloc[0:5, :5])

print(data_all[0].columns.tolist())

print(data_all[0]['B365H'][:30])


print('https://www.football-data.co.uk/mmz4281/' +'2425' + '/' + 'E0' + '.csv')

leagues2 = ['E0', 'E1', 'E2', 'E3', 'EC']
frames = []

root = 'https://www.football-data.co.uk/mmz4281/'
for league in leagues2:
    df = pd.read_csv(root + '2425' + '/' + league + '.csv')
    frames.append(df)

print(frames)
print(len(frames))
print(frames[0])

leagues = ['E0', 'E2', 'E3']
frames = []

print('__________')
for league in leagues:
    for season in range(18, 24):
        df = pd.read_csv(root + str(season) + str(season+1) + '/' + league + '.csv', encoding = 'latin1')
        df.insert(1, 'season', season) # Als 2. Spalte die Saison, das Jahr in dem die Saison beginnt.
        frames.append(df)

print(len(frames))

print(frames[0])

df = frames[0]

# Kopie des DataFrames für separate Bearbeitung
df_home = df[['HomeTeam', 'FTHG', 'FTAG']].copy()
df_away = df[['AwayTeam', 'FTHG', 'FTAG']].copy()

# Umbenennen für konsistente Verarbeitung
df_home.columns = ['Team', 'GoalsFor', 'GoalsAgainst']
df_away.columns = ['Team', 'GoalsAgainst', 'GoalsFor']  # Auswärts: Tore umgekehrt

# Punkte berechnen
df_home['Points'] = df_home.apply(lambda row: 3 if row.GoalsFor > row.GoalsAgainst else (1 if row.GoalsFor == row.GoalsAgainst else 0), axis=1)
df_away['Points'] = df_away.apply(lambda row: 3 if row.GoalsFor > row.GoalsAgainst else (1 if row.GoalsFor == row.GoalsAgainst else 0), axis=1)

print(df_home)

# Alles zusammenfügen
df_all = pd.concat([df_home, df_away], ignore_index=True)
print(df_all)


# Gruppieren & zusammenfassen
table = df_all.groupby('Team').agg(
    Matches=('Points', 'count'),
    Wins=('Points', lambda x: (x == 3).sum()),
    Draws=('Points', lambda x: (x == 1).sum()),
    Losses=('Points', lambda x: (x == 0).sum()),
    GoalsFor=('GoalsFor', 'sum'),
    GoalsAgainst=('GoalsAgainst', 'sum'),
    Points=('Points', 'sum')
)
print('*****')
print(table)
# Tordifferenz berechnen
table['GoalDiff'] = table['GoalsFor'] - table['GoalsAgainst']

# Sortieren nach Punkten, dann Tordifferenz
table = table.sort_values(by=['Points', 'GoalDiff'], ascending=False)

# Index zurücksetzen für schöne Ausgabe
table = table.reset_index()

print(table)

import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Clothing'],
    'sales': [1200, 900, 1500, 600, 750]
})

# Group by category and calculate mean sales
grouped_sales = df.groupby('category')['sales'].mean()
print(grouped_sales)

# Multiple aggregation methods
multi_agg = df.groupby('category').agg(
    Test = ('sales', 'mean'),
    Summe = ('sales', 'sum'),
    Anzahl = ('sales', 'count'),
    Groesser800 = ('sales', lambda x: (x > 800).sum())
)
print(multi_agg)

# Custom transformation
def sales_difference(x):
    return x - x.mean()

group_transform = df.groupby('category')['sales'].transform(sales_difference)
print(group_transform)

print('-------------')

dict_countries = {
    'Spanish La Liga': 'SP1', 'Spanish Segunda Division': 'SP2',
    'German Bundesliga': 'D1', 'English Premier League': 'E0',
    'English League 1': 'E2', 'English League 2': 'E3'
}

print(dict_countries['Spanish La Liga'])

dict_historical_data = {}

# leagues = ['E0', 'E2', 'E3']


for league in dict_countries:
    frames = []
    for season in range(18, 24):
        df = pd.read_csv(root + str(season) + str(season+1) + '/' + dict_countries[league] + '.csv', encoding = 'latin1')
        df.insert(1, 'season', season) # Als 2. Spalte die Saison, das Jahr in dem die Saison beginnt.
        frames.append(df)
    df_concat = pd.concat(frames)
    dict_historical_data[league] = df_concat

print(dict_historical_data)
print(len(dict_historical_data))
print(dict_historical_data.keys())
print(dict_historical_data['English Premier League'])
print(dict_historical_data['English Premier League'])
print(dict_historical_data['English Premier League'][dict_historical_data['English Premier League']['season']==18])











