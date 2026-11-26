
import pandas as pd
import numpy as np

# Make random data reproducible
np.random.seed(42)

# Number of sales records
n = 350

# Create dataset
data = {
    "Order_ID": range(1001, 1001 + n),

    "Date": pd.date_range(
        start="2026-01-01",
        periods=n,
        freq="D"
    ),

    "Product": np.random.choice(
        ["Laptop", "Mobile", "Headphones", "Tablet", "Smartwatch"],
        n
    ),

    "Category": np.random.choice(
        ["Electronics", "Accessories", "Gadgets"],
        n
    ),

    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        n
    ),

    "Quantity": np.random.randint(1, 6, n),

    "Price": np.random.choice(
        [500, 1000, 1500, 2000, 3000, 5000],
        n
    )
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Save dataset
df.to_csv("sales_data.csv", index=False)

print("Sales dataset created successfully!")
print(df.head())
print("\nTotal Records:", len(df))
