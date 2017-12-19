import pandas as pd
import re

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
total = data["total_enrollment"].sum()

races = {
"HI": "Hispanic",
"AM": "American Indian",
"AS": "Asian",
"HP": "Hawaiian or Pacific Islander",
"BL": "Black",
"WH": "White",
"TR": "Two or more races"
}

race_enr = {}

for col in data.columns:
    if re.match("SCH_ENR_.._[FM]", col) is None:
        pass
    else:
        rc = col.replace("SCH_ENR_", "").replace("_M", "").replace("_F", "")
        if races[rc] in race_enr:
            race_enr[races[rc]] += data[col].sum() / total
        else:
            race_enr[races[rc]] = data[col].sum() / total
        
print(race_enr)