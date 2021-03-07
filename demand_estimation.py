#%%
import pandas as pd 
import numpy as np

#%%
dist = pd.read_csv('distribution.csv')
dist

#%%
times = 506/90/87*20000
times

# %%
peak_times = times*0.46
peak_times

# %%
dist['times'] = dist['ratio'] * peak_times
dist[dist['times']>1]

# %%
dist