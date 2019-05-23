# Pandas for managing datasets
import pandas as pd

# Display floats with 2 decimal places
pd.options.display.float_format = '{:,.2f}'.format

# Expand display limits
pd.options.display.max_rows = 200
pd.options.display.max_columns = 100

# Read BNC2 dataset
df = pd.read_csv('/home/bizviz/Downloads/BNC2_sample.csv',names=['Code','Date','Open','High','Low','Close','Volume','VWAP','TWAP'])

# Display first 5 observation
df.head()

# Unique code in the dataset
print(df.Code.unique())

# Example of GWA and MWA relationship
df[df.Code.isin(['GWA_BTC','MWA_BTC_JPY','MWA_BTC_EUR',]) & (df.Date == '2018-01-01')]

# Number of observation
print('Before : ',len(df))

# Get all the GWA codes
gwa_codes = [code for code in df.Code.unique() if 'GWA_' in code]

# Only keep GWA observation
df = df[df.Code.isin(gwa_codes)]

# Number of observation left
print('After : ',len(df))

# Pivote datasets
pivoted_df = df.pivot(index='Date',columns='Code',values='VWAP')

# Display examples from pivoted datasets
pivoted_df.tail()

# shifts the index of the dataframe by some number of periods.
print( pivoted_df.tail(3) )

print( pivoted_df.tail(3).shift(1) )

# Calculate returns over 7 days prior
delta_7 = pivoted_df / pivoted_df.shift(7) - 1.0

# Display examples
delta_7.tail()

# Calculate returns over each windows add store then in dictionary
delta_dict = {}
for offset in [7,14,21,28]:
    delta_dict['delta{}'.format(offset)] = pivoted_df /pivoted_df.shift(offset) - 1.0


# Melt delta_7 returns
melted_7 = delta_7.reset_index().melt(id_vars=['Date'],value_name='delta_7')


# Melted dataframe example
melted_7.tail()


# Melt all the delta dataframes and store in list
melted_dfs = []
for key, delta_df in delta_dict.items():
    melted_dfs.append(delta_df.reset_index().melt(id_vars=['Date'],value_name=key))


# Calculate 7-day returns after the date
return_df = pivoted_df.shift(-7) / pivoted_df - 1.0


# Melt the return dataset and append to list
melted_dfs.append( return_df.reset_index().melt(id_vars=['Date'], value_name='return_7') )
