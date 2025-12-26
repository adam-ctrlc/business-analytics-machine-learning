import pandas as pd
import numpy as np

base_path = "./excel/"
excel_file_path = f"{base_path}/data.xlsx"

raw_data = pd.read_excel(excel_file_path)
data = raw_data.drop(columns=['post_id'])

for words in data.index:
    curr_val_title = data.at[words, 'title']
    new_val_title = len("".join(curr_val_title.split()))
    data.at[words, 'title'] = new_val_title

    curr_val_desc = data.at[words, 'description']
    new_val_desc = len("".join(curr_val_desc.split()))
    data.at[words, 'description'] = new_val_desc


data.to_excel('./excel/data_cleaned.xlsx', index=False)
