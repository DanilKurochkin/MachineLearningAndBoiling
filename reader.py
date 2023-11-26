import pandas as pd
import numpy as np

def from_txt(filepath : str) -> pd.DataFrame: 
    with open(filepath, mode='r') as file:
        strings = file.readlines()
    
    stripped = strings[0].replace(',', '').rstrip().split()
    columns = []
    for i in range(len(stripped)//2):
        columns.append(f'{stripped[2*i]} {stripped[2*i+1]}')
    
    rows = []
    for i in range(1, len(strings)):
        stripped = strings[i].replace(',' , '.').rstrip().split()
        row = []
        for i in range(len(stripped)):
            row.append(float(stripped[i]))
        rows.append(row)
    
    return pd.DataFrame(data=rows, columns=columns)
    