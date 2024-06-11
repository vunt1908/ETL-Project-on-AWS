import pandas as pd

df = pd.read_csv(r'C:\Users\NITRO 5\Documents\Dev\DE\DWH\customer_data_transformed.csv')

df_extracted = df.head(2000)

df_extracted.to_csv('customer_data_extract_2000.csv', index=False)
