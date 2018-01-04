import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("sphist.csv")
data["Date"] = pd.to_datetime(data["Date"])
data = data.sort_values("Date", ascending=True)

day_5 = data["Close"].rolling(window=5,center=False).mean() 
day_30 = data["Close"].rolling(window=30,center=False).mean() 
day_365 = data["Close"].rolling(window=365,center=False).mean() 
indicators = pd.DataFrame(data={"day_5": day_5, "day_30": day_30, "day_365": day_365})
indicators = indicators.shift(1)
indicators = pd.concat([data[["Date", "Close"]], indicators], axis=1)
indicators = indicators.dropna()

train = indicators[indicators["Date"] < datetime(year=2013, month=1, day=1)]
test = indicators[indicators["Date"] >= datetime(year=2013, month=1, day=1)]

model = LinearRegression()
model.fit(train[["day_5", "day_30", "day_365"]], train["Close"])
y_pred = model.predict(test[["day_5", "day_30", "day_365"]])

rmse = mean_squared_error(test["Close"], y_pred)
print(rmse)

