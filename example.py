# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df = pd.DataFrame([[2,5,3],[1,8,4]])
print(df)

log_df = np.log(df)

mult_df = log_df * 2