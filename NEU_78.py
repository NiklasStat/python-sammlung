import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_laptops = pd.read_csv('laptop_price.csv', encoding='latin1')
print(df_laptops.head(3))


dd = df_laptops['Company']=="Apple"
print(dd.sum())
print(len(dd))

apple_rows = df_laptops[df_laptops['Company'] == "Apple"]
print(apple_rows.index.tolist())

print(df_laptops[dd])
print(df_laptops[dd].value_counts('Company'))


no_HP_rows = df_laptops[df_laptops['Company'] != "HP"]
print(df_laptops[df_laptops['Company'] != "HP"].value_counts('Company'))

print(no_HP_rows.index.tolist())

laptops_2000_rows = df_laptops[df_laptops['Price_euros'] > 2000]
print(laptops_2000_rows)

print(df_laptops['Price_euros'] > 2000)

df_laptops['Price_tier'] = np.where(df_laptops['Price_euros'] > 2000, 'Expensive', 'Cheap')
print(df_laptops.head())
print(df_laptops.value_counts('Price_tier'))

print(len(df_laptops[df_laptops['Inches'] > 15]))
df_laptops['Size30+'] = np.where(df_laptops['Inches'] > 15, 'Big', 'Small')
print(df_laptops.head())
print(df_laptops['Size30+'].value_counts())

print(df_laptops[(df_laptops['Company'] == 'Apple') & (df_laptops['Price_tier'] == 'Expensive')])

# and -> &  in PANDAS !!!!!!!!!!!!!!!
# or |



print((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell'))

print(df_laptops[(df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')].value_counts('Company'))

print(df_laptops[((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')) & (df_laptops['Price_euros'] > 2000)].value_counts('Company'))

conditions = [
    df_laptops['Price_euros'] > 3000,
    (df_laptops['Price_euros'] > 2000) & (df_laptops['Price_euros'] <= 3000),
    (df_laptops['Price_euros'] > 800) & (df_laptops['Price_euros'] <= 2000),
    df_laptops['Price_euros'] <= 800
]

values = ['Too Expensive', 'Expensive', 'Affordable', 'Cheap']

df_laptops['Preiskat'] = np.select(conditions, values, default='Unbekannt')
print(df_laptops['Preiskat'].value_counts())



conditions = [
    df_laptops['Inches'] > 16,
    (df_laptops['Inches'] > 14) & (df_laptops['Inches'] <= 16),
    (df_laptops['Inches'] > 12) & (df_laptops['Inches'] <= 14),
    df_laptops['Inches'] <= 12
]

values = ['Too Big', 'Big', 'Small', 'Too Small']

df_laptops['Groesse4'] = np.select(conditions, values, default='Unbekannt')
print(df_laptops['Groesse4'].value_counts())

print('----------------')
print(df_laptops['Company'].isin(['Apple', 'HP']))
print(df_laptops[df_laptops['Company'].isin(['Apple', 'HP'])].value_counts('Company'))

filter1 = df_laptops['TypeName'].isin(['Notebook', 'Ultrabook'])
filter2 = df_laptops['Company'].isin(['Apple', 'HP'])

print(df_laptops[filter1 & filter2].iloc[0:10,0:5])

print(df_laptops.duplicated('laptop_ID'))

print(df_laptops[df_laptops.duplicated('laptop_ID')])

print(df_laptops.duplicated(['Product', 'TypeName', 'Inches']))

print(df_laptops.duplicated(['Product', 'TypeName', 'Inches']).sum())

print(df_laptops[df_laptops.duplicated(['Product', 'TypeName', 'Inches'])].iloc[0:10, 0:5])

duplicated = df_laptops.duplicated(['Product', 'TypeName', 'Inches'])

print('++++++++')
print(df_laptops[duplicated].sort_values(['Product', 'TypeName']))

df_laptops = df_laptops.sort_values(['Company', 'Price_euros'])
print(df_laptops[['Price_euros', 'Company']])

print(df_laptops.value_counts('Company'))
duplicated_first = df_laptops.duplicated('Company', keep = 'first')

print(df_laptops[duplicated_first])

print(df_laptops[~duplicated_first]) # opposite

data_test = {
    'Name': ['Anna', 'Ben', 'Clara', 'Anna', 'Nik', 'Anna'],
    'Alter': [25, 30, 27, 28, 31, 25],
    'Stadt': ['Berlin', 'Köln', 'Hamburg', 'München', 'Stuttgart', 'Berlin']
}

df = pd.DataFrame(data_test)
print(df)

print(df.duplicated('Name'))
print(df[df.duplicated('Name')])
print(df[~df.duplicated('Name')])

print(df_laptops[~duplicated_first]) # opposite

# laptops with cheapest price since 1st value of sorted list was
# cheapest of Company and others are dupicats and deleted

print(df_laptops[~duplicated_first][['Company', 'Price_euros']])

print(df_laptops[~duplicated_first].value_counts('Company'))

# get last duplicated value
duplicated_last = df_laptops.duplicated('Company', keep = 'last')

print(df_laptops[~duplicated_last][['Company', 'Price_euros']])

print('------')

duplicated_false = df_laptops.duplicated('Company', keep = False)


# empty since only duplicated values
print(df_laptops[~duplicated_false][['Company', 'Price_euros']])
# proof
print(df_laptops.value_counts('Company'))

print(df_laptops.drop_duplicates(['Company'])[['Company', 'Price_euros']].value_counts('Company'))

df_laptops = df_laptops.sort_values(['Company', 'Price_euros'])
print(df_laptops.drop_duplicates(['Company'], keep = 'first')[['Company', 'Price_euros']])
df_laptops.drop_duplicates(['Company'], keep = 'last', inplace = True, ignore_index = True)
print(df_laptops[['Company', 'Price_euros']])

