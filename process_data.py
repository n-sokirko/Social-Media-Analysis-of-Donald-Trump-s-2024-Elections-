# process_data.py

import pandas as pd

def save_data_to_json(user_data, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(user_data, f)

def load_data_from_json(filename):
    import json
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def convert_data_to_dataframe(user_data):
    df = pd.DataFrame(user_data)
    df['date'] = pd.to_datetime(df['created_utc'], unit='s')
    df['day'] = df['date'].dt.date
    return df
