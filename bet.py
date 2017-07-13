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
path, filename = os.path.split(file_path)

fsl.FSLCommand.set_default_output_type('NIFTI')
example_nii = fnmatch.filter(os.listdir(path), '*.nii')
print example_nii
for x in range(0, len(example_nii)):
	btr = fsl.BET()
	btr.inputs.in_file = path + "/" + example_nii[x]
	btr.inputs.out_file = path + "/res/" + "BET_7" + "_" + example_nii[x]
	btr.inputs.frac = 0.7
	res = btr.run()
