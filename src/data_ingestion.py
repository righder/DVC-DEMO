import pandas as pd
import os
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/araJ2/customer-database/master/Ecommerce%20Customers.csv")

# Drop unnecessary columns
df = df.drop(df.columns[:3], axis=1)


# Keep rows where length of membership > 3
df = df[df['Length of Membership'] > 3]

# Drop rows with missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert object columns to category dtype
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category')

df.to_csv("data/customer.csv", index=False)

df.drop(df.columns[:3], axis=1, inplace=True)                                                                                   