# Importē nepieciešamo bibliotēku
import pandas as pd

#CSV faila lokācija
csv_file_path = 'C:/Users/kikap/Downloads/algor/openipf.csv'
f = pd.read_csv(csv_file_path)

# Filtrē csv failu pēc uzdevuma prasībām (vecums zem 20 un bench lielāks par 105 kg)
df = f[(f['Age'] < 20) & (f['Best3BenchKg'] > 105)]

# Paņem uzdevuma dotās kolonas (dalībnieku vārdi, vecums, svara kategorija, lielākais bench lifts un dalībnieka valsts)
columns = ['Name', 'Age', 'WeightClassKg', 'Best3BenchKg', 'Country']
df = df[columns]

# Filtrē excel failu no zemāka vecuma uz augšu 
df = df.sort_values(by='Age')

# Excel faila lokācija 
output_excel_path = 'C:/Users/kikap/Downloads/algor/ipfdalibnieki.xlsx'

# Saglabā excel failu
df.to_excel(output_excel_path, index=False)

print('Fails izveidots', output_excel_path)
