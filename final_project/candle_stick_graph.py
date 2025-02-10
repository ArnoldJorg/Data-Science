import pandas as pd
import plotly.graph_objects as go

# Load your data
df = pd.read_csv("bitcoin_historical_data.csv", sep=";")
df["timeOpen"] = pd.to_datetime(df["timeOpen"])

fig = go.Figure(
    data=[
        go.Candlestick(
            x=df["timeOpen"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            increasing_line_color="green",
            decreasing_line_color="red",
        )
    ]
)

fig.update_layout(
    title="Bitcoin Price Movements 2024-2025",
    xaxis_title="Date / Time",
    yaxis_title="Price (USD)",
    xaxis_rangeslider_visible=False,
)

fig.show()
