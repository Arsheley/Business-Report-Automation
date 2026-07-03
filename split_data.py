import pandas as pd
import os
data = pd.read_csv('raw_data/Sales_Data.csv')
data["Order Date"] = pd.to_datetime(data["Order Date"])
data["Month Name"] = data["Order Date"].dt.month_name()

os.makedirs("input_reports", exist_ok=True)
data = data.sort_values('Order Date')
for month, month_data in data.groupby("Month Name",sort=False):
   month_number = month_data["Order Date"].dt.month.iloc[0]
   month_data.to_excel(f"input_reports/{month_number:02d}_{month}.xlsx", index=False)

print("Monthly Excel files created successfully!") 