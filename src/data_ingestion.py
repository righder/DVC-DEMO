import pandas as pd
import os
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/araJ2/customer-database/master/Ecommerce%20Customers.csv")

# Drop unnecessary columns
df = df.drop(df.columns[:3], axis=1)

#length of membership > 3 we keep
df = df[df['Length of Membership'] > 3]

df.to_csv("data/customer.csv", index=False)