# Laptop Price Analysis with MySQL, Pandas & Seaborn

# Import required libraries
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean seaborn style for all charts
sns.set(style="whitegrid", palette="muted")


# 1. Connect to MySQL Database
engine = create_engine(
    "mysql+mysqlconnector://root:Rukesh%40123@127.0.0.1:3306/laptop_db"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT DATABASE();"))
    for row in result:
        print("✅ Connected to Database:", row[0])


# 2. Load and Prepare the Dataset
df = pd.read_csv("data/laptop_price.csv", encoding="latin1")
print("\nDataset Loaded Successfully!")
print("Shape:", df.shape)
print(df.head())

df["Price_INR"] = df["Price_euros"] * 140
df["Weight_kg"] = df["Weight"].str.replace("kg", "").astype(float)

print("\nSample after currency & weight conversion:")
print(df[["Company", "Price_euros", "Price_INR", "Weight_kg"]].head())


# 3. Store Cleaned Data into MySQL
df.to_sql("laptops_cleaned_inr", con=engine, if_exists="replace", index=False)
print("✅ Cleaned data stored in MySQL (table: laptops_cleaned_inr)")

df = pd.read_sql("SELECT * FROM laptops_cleaned_inr", con=engine)
print("Pulled from MySQL. Shape:", df.shape)


# 4. Analysis & Visualizations


# Average Laptop Price by Brand
avg_price = df.groupby("Company")["Price_INR"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price.index, y=avg_price.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Average Laptop Price by Brand (INR)")
plt.ylabel("Average Price (INR)")
plt.savefig("avg_price_by_brand.png")
plt.show()

# Price Distribution
plt.figure(figsize=(8, 6))
sns.histplot(df["Price_INR"], bins=30, kde=True)
plt.title("Laptop Price Distribution in INR")
plt.xlabel("Price (INR)")
plt.savefig("price_distribution.png")
plt.show()

# Correlation between RAM, Weight, and Price
df["Ram_GB"] = df["Ram"].str.replace("GB", "").astype(int)

plt.figure(figsize=(8, 6))
sns.heatmap(df[["Ram_GB", "Weight_kg", "Price_INR"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# Top 5 Most Expensive Laptops
top5 = df.nlargest(5, "Price_INR")

plt.figure(figsize=(8, 6))
sns.barplot(x="Product", y="Price_INR", data=top5, palette="magma")
plt.title("Top 5 Most Expensive Laptops")
plt.xticks(rotation=45)
plt.savefig("top5_expensive.png")
plt.show()

# Laptops in the Mid-Range (₹50k–₹80k)
mid_range = df[(df["Price_INR"] >= 50000) & (df["Price_INR"] <= 80000)]
print(f"\n💻 Mid-range laptops (₹50k–₹80k): {len(mid_range)} models found")
print(mid_range[["Company", "Product", "Price_INR", "Ram"]].head())

# Operating System Distribution
plt.figure(figsize=(6, 6))
df["OpSys"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Operating System Distribution")
plt.savefig("os_distribution.png")
plt.show()

# RAM vs Price Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Ram_GB", y="Price_INR", data=df, hue="Company")
plt.title("RAM vs Price (INR)")
plt.savefig("ram_vs_price.png")
plt.show()


# 5. Save Outputs
mid_range.to_csv("filtered_laptops.csv", index=False)
print("✅ Filtered mid-range dataset saved (filtered_laptops.csv)")

print("\n✨ Analysis Complete! All plots and filtered data have been saved.")
