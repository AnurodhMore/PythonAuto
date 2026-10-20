import pandas as pd



test = pd.read_csv("https://football-data.co.uk/mmz4281/2627/E0.csv")
print(test)

test.rename(columns={'FTHG: 0':'home_goals', 'FTAG':'away_goals'}, inplace=True)
print(test)


