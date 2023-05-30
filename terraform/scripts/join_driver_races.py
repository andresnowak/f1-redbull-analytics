import pandas as pd

df_1 = pd.read_csv("./data/driver_standings_2.csv")
df_2 = pd.read_csv("./data/races_2.csv")
df_3 = pd.read_csv("./data/drivers_2.csv")

df_2.drop(["url"], inplace=True, axis=1)

df_4 = pd.merge(df_1, df_2, how='inner', on=['raceId'])
df_5 = pd.merge(df_3, df_4, how='inner', on=['driverId'])

df_5.to_csv("./data/driver_standings.csv", index=False)
