import pandas as pd

with open('Shipping.json') as f:
    df = pd.read_json(f)

df.to_csv('Shipping.csv', index=False)