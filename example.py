# -*- coding: utf-8 -*-
'''
@author Mike Swirsky
'''

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create data

df = pd.DataFrame(columns=['A', 'B', 'C'])

for col in df.columns:
    df[col] = np.random.lognormal(size=1000)

df['D'] = df['A'] * df['B']

# Doing some math

log_df = np.log(df)
# mult_df = log_df * 2

# Printing output

print('log_df')
print(log_df.head())

sns.scatterplot('C', 'D', data=log_df)
plt.title('Example Scatter Plot')
plt.show()
