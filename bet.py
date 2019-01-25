import os
import fnmatch
import nipype.interfaces.fsl as fsl
from Tkinter import Tk
from tkFileDialog import askopenfilename

#path = "/home/antogeo/Dropbox/current_work/tmp/frst/"
root = Tk()
root.update()
root.withdraw()
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
f_path, filename = os.path.split(file_path)

fsl.FSLCommand.set_default_output_type('NIFTI')
example_nii = fnmatch.filter(os.listdir(f_path), '*.nii')
print example_nii
for name in example_nii:
	btr = fsl.BET()
	btr.inputs.in_file = os.path.join(f_path, name)
	btr.inputs.out_file = os.path.join(f_path, res, "BET7_" + name)
	btr.inputs.frac = 0.7
	res = btr.run()
