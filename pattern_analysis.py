import talib
import yfinance as yf

"""
returns a DataFrame
"""
data = yf.download("ETH-USD", start="2022-01-01", end="2023-01-01")

"""
Detect morning star 
"""
morning_star = talib.CDLMORNINGSTAR(
    data["Open"], 
    data["High"],
    data["Low"],
    data["Close"]
)

"""
Detect engulfing
"""
engulfing = talib.CDLENGULFING(
    data["Open"], 
    data["High"],
    data["Low"],
    data["Close"]
)

"""
Add columns to the DataFrame
"""
data["Morning Star"] = morning_star
data["Engulfing"] = engulfing

nz_morning_stars = data[data["Morning Star"] != 0]
print(nz_morning_stars)

nz_engulfing = data[data["Engulfing"] != 0]
print(nz_engulfing)