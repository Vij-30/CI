import pandas as pd

symbols = ['Ž', 'Š', 'œ']

def load_and_clean(filename, encoding, sep=','):
    # Read file with no header assumed, but try to guess if header exists
    df = pd.read_csv(filename, encoding=encoding, sep=sep)
    
    # If columns names are not symbol and value, rename them
    if df.columns[0].lower() != 'symbol':
        df.columns = ['symbol', 'value']
    
    # Strip whitespace from symbols
    df['symbol'] = df['symbol'].astype(str).str.strip()
    
    # Convert 'value' to numeric, coerce errors (turn invalid to NaN)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    
    # Drop rows where value is NaN (non-numeric)
    df = df.dropna(subset=['value'])
    
    return df

# Load the files correctly with separators and encodings
df1 = load_and_clean('data1.csv', encoding='cp1252', sep=',')
df2 = load_and_clean('data2.csv', encoding='utf-8', sep=',')
df3 = load_and_clean('data3.txt', encoding='utf-16', sep='\t')

# Filter rows for symbols of interest and sum values
sum1 = df1[df1['symbol'].isin(symbols)]['value'].sum()
sum2 = df2[df2['symbol'].isin(symbols)]['value'].sum()
sum3 = df3[df3['symbol'].isin(symbols)]['value'].sum()

total_sum = sum1 + sum2 + sum3

print(f"Total sum for symbols Ž, Š, œ: {total_sum}")

