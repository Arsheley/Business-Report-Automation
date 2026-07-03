import pandas as pd
import os
def read_reports():
    files = os.listdir("input_reports")

    #print('o')
    all_data = []

    for file in files:
        data = pd.read_excel(f"input_reports/{file}")
        all_data.append(data)

    #print(len(all_data))
    combined_data = pd.concat(all_data, ignore_index=True)
    return combined_data
    #print(combined_data.head())
