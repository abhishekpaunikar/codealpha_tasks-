
# ✅ Unemployment Analysis with Python - CodeAlpha Internship

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Create sample data inline (no CSV needed)
data = {
    "Date": [
        "2020-01-01", "2020-02-01", "2020-03-01", "2020-04-01",
        "2020-05-01", "2020-06-01", "2020-07-01", "2020-08-01",
        "2020-09-01", "2020-10-01"
    ],
    "Unemployment_rate": [6.1, 6.3, 7.0, 8.5, 9.0, 8.0, 7.3, 6.8, 6.5, 6.0]
}

# ✅ Load data into DataFrame
df = pd.DataFrame(data)

# ✅ Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# ✅ Print first few rows
print("📊 First 5 rows:")
print(df.head())

# ✅ Describe the dataset
print("\n📈 Statistical Summary:")
print(df.describe())

# ✅ Correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ✅ Distribution plot of Unemployment Rate
sns.histplot(df['Unemployment_rate'], kde=True, color='skyblue')
plt.title("Unemployment Rate Distribution")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.show()

# ✅ Unemployment rate over time
plt.plot(df['Date'], df['Unemployment_rate'], marker='o', color='red')
plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ COVID-19 analysis (2020)
covid_df = df[(df['Date'] >= '2020-01-01') & (df['Date'] <= '2020-12-31')]

if not covid_df.empty:
    sns.lineplot(x='Date', y='Unemployment_rate', data=covid_df, marker='o', color='purple')
    plt.title("Unemployment Rate During COVID-19 (2020)")
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()
else:
    print("⚠️ No COVID-19 period data found.")
