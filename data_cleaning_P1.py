import pandas as pd

# 1. Messy data of receipts
df = pd.read_csv('raw_supermarket_data.csv')

print("--- Spotting the Mess ---")
print(df.isnull().sum()) # Counts of blank spaces in each column

# 2. Fixing the Impossible Negative Sales
# Using .abs() (absolute value) to turn any negative numbers into positive ones.
df['Units_Sold'] = df['Units_Sold'].abs()

# 3. The Missing Prices
# Assuming a standard 50% markup on the Unit_Cost for any missing Unit_Price.
df['Unit_Price'] = df['Unit_Price'].fillna(df['Unit_Cost'] * 1.5)

# 4. The Core Financials
df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']
df['Total_Cost'] = df['Units_Sold'] * df['Unit_Cost']
df['Gross_Profit'] = df['Total_Revenue'] - df['Total_Cost']

print("\n--- Verifying the Cleanup ---")
print(df.isnull().sum()) 
print("\nSuccess! Here are your fresh financial columns:")
print(df[['Transaction_ID', 'Total_Revenue', 'Gross_Profit']].head(5))

df.to_csv('clean_supermarket_data.csv', index=False)
