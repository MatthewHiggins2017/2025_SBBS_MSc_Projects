'''
Goal: Add random codes to the project 

'''

import pandas as pd 

df = pd.read_csv('./docs/data/Projects.tsv',sep='\t')

# Assign Code based on position starting from B2000, fitting within 5 characters (B2 + 3 digits)
# This allows for up to 1000 unique codes: B2000 to B2999
df['Assigned_Code'] = 'B2' + df.index.astype(str).str.zfill(3)

# Save the updated dataframe back to the file
df.to_csv('./docs/data/Projects.tsv', sep='\t', index=False)



