import pandas as pd

def Retrieve_names(file_path: str) -> list:
    ''''''

    df = pd.read_excel(file_path)
    return df["Names"].tolist()


file_path = 'Occupants.xlsx'

Retrieve_names(file_path)