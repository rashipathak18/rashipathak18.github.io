
import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Calculate important business metrics
total_revenue = df["Revenue"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_revenue / total_orders

# Find best-selling product
top_product = df.groupby("Product")["Revenue"].sum().idxmax()

# Find best-performing region
top_region = df.groupby("Region")["Revenue"].sum().idxmax()

# Display results
print("\n------ SALES ANALYSIS ------")

print("Total Revenue: ₹", total_revenue)
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)

print("Average Order Value: ₹", round(average_order_value, 2))

print("Top Selling Product:", top_product)
print("Best Performing Region:", top_region)
