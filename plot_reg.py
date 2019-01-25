from pypet import mask
import os.path as op
import os
from glob import glob
import nibabel as nib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# create csv files using compute_parc.py

df_ctrl = pd.read_csv('results/values_ctrl.csv')
df_subj = pd.read_csv('results/values_subj.csv')

all_df = pd.concat([df_subj, df_ctrl], ignore_index=True)

all_df = pd.DataFrame(all_df)

f, axes = plt.subplots(3, 1)
ax = sns.barplot(x="n_reg", y="mean_val", hue='session',
                 data=all_df, ax=axes[0])
ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
ax1 = sns.pointplot(x="n_reg", y="mean_val", hue="session",
                    data=all_df, ax=axes[1])
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=30)
ax2 = sns.lineplot(x="n_reg", y="mean_val", hue="session",
                   data=all_df, ax=axes[2])
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=30)
