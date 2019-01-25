import sys
import os
import os.path as op
from fnmatch import filter as ffilter
from tkinter import *
from tkinter.filedialog import askopenfilename
from nipype.interfaces.ants import Registration

template = '/home/coma_meth/Desktop/test/ants/single_subj_T1.nii' #askopenfilename('/home/antogeo/Documents/MATLAB/spm12/canonical/avg152T1.nii') # show an "Open" dialog box and return the path to the selected file
# print(filename)
path = "/home/coma_meth/Desktop/test/ants/res/"
subj_volname = ffilter(os.listdir(path), '*.nii')

# Mandatory
reg = Registration()
reg.inputs.fixed_image = template
reg.inputs.transforms = ['Translation', 'Rigid', 'Affine', 'Syn']
reg.inputs.smoothing_sigmas = [[4, 2, 1]] * 3 + [[1, 0.5, 0]]
reg.inputs.metric = ['Mattes'] * 3 + [['Mattes', 'CC']]
reg.inputs.metric_weight = [1] * 3 + [[0.5, 0.5]]
reg.inputs.shrink_factors = [[6, 4, 2]] + [[3, 2, 1]] * 2 + [[4, 2, 1]]

# Optional
reg.inputs.transform_parameters = [(0.1,), (0.1,), (0.1,), (0.2, 3.0, 0.0)]
reg.inputs.number_of_iterations = ([[10000, 111110, 11110]] * 3 + [[100, 50, 30]])
reg.inputs.dimension = 3
reg.inputs.write_composite_transform = True
reg.inputs.collapse_output_transforms = False
reg.inputs.radius_or_number_of_bins = [32] * 3 + [[32, 4]]
reg.inputs.sampling_strategy = ['Regular'] * 3 + [[None, None]]
reg.inputs.sampling_percentage = [0.3] * 3 + [[None, None]]
reg.inputs.convergence_threshold = [1.e-8] * 3 + [-0.01]
reg.inputs.convergence_window_size = [20] * 3 + [5]
reg.inputs.sigma_units = ['vox'] * 4
reg.inputs.use_estimate_learning_rate_once = [True] * 4
reg.inputs.use_histogram_matching = [False] * 3 + [True]
reg.inputs.initial_moving_transform_com = True
reg.inputs.interpolation= ['BSpline']

for subj in subj_volname:
	reg.inputs.moving_image = op.join(path, subj)
	reg.inputs.output_transform_prefix = subj + "_"
	reg.inputs.output_warped_image =  op.join(path, subj + '_WARPED.nii.gz')
  reg.run()
