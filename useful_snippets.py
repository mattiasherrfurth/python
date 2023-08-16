# common string methods
.find()
.join()
.lower()
.upper()
.strip()
.split()
.replace()
.endswith()
.isalnum()
.isalpha()
.isdigit()

# common pandas objects/methods
.shape
.head()
.tail()
.describe()
.columns
.dtypes
.unique()
.groupby()
.sample()
.drop()
.dropna()
.fillna()
.insert()
.loc()
.sort_values()
.iterrows()
.apply()
.pivot()
.transpose()
.melt()

# pandas set options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# pandas add boolean column checking for substring in existing column
df_names['new_col'] = df_names['string_col'].map(lambda x: True if 'substring' in str(x).lower() else False)

# pandas add list as row to end of dataframe
df.loc[len(df)] = [list,of,values]

# pandas count group by column
df2 = df.groupby(['column'])['column'].count()