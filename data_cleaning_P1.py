import pandas as pd

# 1. Load the messy box of receipts
df = pd.read_csv('raw_supermarket_data.csv')

print("--- Spotting the Mess ---")
print(df.isnull().sum()) # This counts how many blank spaces exist in each column

# 2. Fix the Impossible Negative Sales
# A cashier typing '-1' instead of '1' is a common typo. 
# We use .abs() (absolute value) to turn any negative numbers into positive ones.
df['Units_Sold'] = df['Units_Sold'].abs()

# 3. Fix the Missing Prices
# Instead of deleting rows with missing prices, we will fill them in (imputation).
# We will assume a standard 50% markup on the Unit_Cost for any missing Unit_Price.
df['Unit_Price'] = df['Unit_Price'].fillna(df['Unit_Cost'] * 1.5)

# 4. Calculate the Core Financials
# Now that the data is clean, we can safely calculate the actual money changing hands.
df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']
df['Total_Cost'] = df['Units_Sold'] * df['Unit_Cost']
df['Gross_Profit'] = df['Total_Revenue'] - df['Total_Cost']

print("\n--- Verifying the Cleanup ---")
print(df.isnull().sum()) # Should show 0 missing values now
print("\nSuccess! Here are your fresh financial columns:")
print(df[['Transaction_ID', 'Total_Revenue', 'Gross_Profit']].head(5))

# 5. Save the sparkling clean data
df.to_csv('clean_supermarket_data.csv', index=False)