### computes and saves in csv file parcelation values of different sessions. With small edit could
# do it for subjects


from pypet import mask
import os.path as op
import os
from glob import glob
import nibabel as nib
import pandas as pd
import numpy as np

if os.uname()[1] == 'antogeo-XPS':
    db_path = enter_path
elif os.uname()[1] == 'comameth':
    db_path = enter_path
sessions = sorted(
    [x.split('/')[-1] for x in glob(op.join(
        db_path, '*')) if op.isdir(op.join(db_path, x))])

# edit atlas path
atlas_fname = op.join(db_path, 'harvOxf_2mm_th25_stspace.nii')
atlas_img = nib.load(atlas_fname)
atlas_flat = np.round(atlas_img.get_data().reshape(-1)).astype(np.int)
values = np.unique(atlas_flat)

df = {}
df['code'] = []
images = []
rois_mean = []
names = []

# edit sessions path
for session in sessions:
    img = glob(op.join(db_path, session, 'niftis', 'sec', 'sk_sc', '*.nii'))
    this_image = nib.load(img[0]).get_data().reshape(-1)
    images.append(this_image)
    names.append(session)

voxels = np.array(images)
atlas_dict = mask.apply_atlas(atlas_fname, voxels)
df_atlas = pd.DataFrame.from_dict(atlas_dict, orient='columns')

sns_df = {}
sns_df['region'] = []
sns_df['session'] = []
sns_df['mean_val'] = []
sns_df['n_reg'] = []
ses_date = ['20170519', '20170804', '20171122', '20180424']
for reg, region in enumerate(df_atlas.columns):
    for i, subj in enumerate(ses_date):
        sns_df['mean_val'].append(df_atlas[region][i])
        sns_df['region'].append(region)
        sns_df['n_reg'].append(reg)
        sns_df['session'].append(i+1)

all_df = pd.DataFrame(sns_df)

all_df.to_csv('results/values_subj.csv')
