import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tokyo_weather.csv")

df.columns = df.columns.str.strip()

df["date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"],
    format="%Y/%m/%d"
)

df["temperature"] = (
    df["temperature"]
    .astype(str)
    .str.replace("(", "-", regex=False)
    .str.replace(")", "", regex=False)
)

df["temperature"] = pd.to_numeric(df["temperature"])

df["humidity"] = pd.to_numeric(df["humidity"])
df["atmospheric pressure"] = pd.to_numeric(df["atmospheric pressure"])

print("TOKYO WEATHER ANALYSIS")
print("=" * 50)

print(f"Number of records: {len(df)}")
print(f"Average Temperature: {df['temperature'].mean():.2f} °C")
print(f"Average Humidity: {df['humidity'].mean():.2f}%")
print(f"Average Atmospheric Pressure: {df['atmospheric pressure'].mean():.2f} hPa")

hottest = df.loc[df["temperature"].idxmax()]
coldest = df.loc[df["temperature"].idxmin()]

print("\nHOTTEST DAY")
print("-" * 20)
print(f"Date: {hottest['date'].date()}")
print(f"Temperature: {hottest['temperature']} °C")

print("\nCOLDEST DAY")
print("-" * 20)
print(f"Date: {coldest['date'].date()}")
print(f"Temperature: {coldest['temperature']} °C")

plt.figure(figsize=(12, 6))

plt.plot(
    df["date"],
    df["temperature"],
    color="red",
    linewidth=2,
    label="Temperature"
)

plt.scatter(
    hottest["date"],
    hottest["temperature"],
    color="darkred",
    s=150,
    label="Hottest Day",
    zorder=5
)

plt.scatter(
    coldest["date"],
    coldest["temperature"],
    color="blue",
    s=150,
    label="Coldest Day",
    zorder=5
)

# Labels
plt.annotate(
    f"Hottest: {hottest['temperature']}°C",
    (hottest["date"], hottest["temperature"]),
    xytext=(10, 10),
    textcoords="offset points"
)

plt.annotate(
    f"Coldest: {coldest['temperature']}°C",
    (coldest["date"], coldest["temperature"]),
    xytext=(10, -15),
    textcoords="offset points"
)

plt.title("Tokyo Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

df["temp_trend"] = df["temperature"].rolling(window=7).mean()

plt.figure(figsize=(12, 6))

plt.plot(
    df["date"],
    df["temperature"],
    color="lightcoral",
    alpha=0.5,
    label="Daily Temperature"
)

plt.plot(
    df["date"],
    df["temp_trend"],
    color="darkred",
    linewidth=3,
    label="7-Day Temperature Trend"
)

plt.title("Tokyo Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

first_trend = df["temp_trend"].dropna().iloc[0]
last_trend = df["temp_trend"].dropna().iloc[-1]

print("\nTEMPERATURE TREND ANALYSIS")
print("-" * 30)

if last_trend > first_trend:
    print("Overall trend: Temperature increased over the recorded period.")
elif last_trend < first_trend:
    print("Overall trend: Temperature decreased over the recorded period.")
else:
    print("Overall trend: Temperature remained stable.")

plt.figure(figsize=(12, 6))

plt.plot(
    df["date"],
    df["humidity"],
    color="blue",
    linewidth=2
)

plt.title("Tokyo Humidity Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

plt.plot(
    df["date"],
    df["atmospheric pressure"],
    color="green",
    linewidth=2
)

plt.title("Tokyo Atmospheric Pressure Over Time")
plt.xlabel("Date")
plt.ylabel("Pressure (hPa)")
plt.grid(True)
plt.tight_layout()
plt.show()

df["month"] = df["date"].dt.month

monthly_temp = df.groupby("month")["temperature"].mean()

plt.figure(figsize=(10, 5))

monthly_temp.plot(
    kind="bar",
    color="orange"
)

plt.title("Average Monthly Temperature in Tokyo")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.grid(axis="y")

plt.tight_layout()
plt.show()

warmest_month = monthly_temp.idxmax()
coldest_month = monthly_temp.idxmin()

print("\nMONTHLY ANALYSIS")
print("-" * 30)
print(f"Warmest Month: {warmest_month} (Average {monthly_temp.max():.2f} °C)")
print(f"Coldest Month: {coldest_month} (Average {monthly_temp.min():.2f} °C)")