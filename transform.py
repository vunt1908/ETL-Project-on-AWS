import pandas as pd

df = pd.read_csv(r'c:\ProgramData\MySQL\MySQL Server 8.0\Uploads\customer.csv')

df['birth_date'] = pd.to_datetime(df['birth_date'], format='%m/%d/%Y').dt.strftime('%d/%m/%Y')
df['opn_dt'] = pd.to_datetime(df['opn_dt'], format='%m/%d/%Y').dt.strftime('%d/%m/%Y')
df['end_dt'] = pd.to_datetime(df['end_dt'], format='%m/%d/%Y').dt.strftime('%d/%m/%Y')

df.to_csv('customer_data_transformed.csv', index=False)
