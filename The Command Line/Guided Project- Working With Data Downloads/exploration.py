import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
pt1 = pd.pivot_table(data, index=["JJ", "SCH_STATUS_MAGNET"], values=["TOT_ENR_M"])
pt2 = pd.pivot_table(data, index=["JJ", "SCH_STATUS_MAGNET"], values=["TOT_ENR_F"])
print(pt1)
print(pt2)
