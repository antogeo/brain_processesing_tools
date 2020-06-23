Import os
import os.path as op
import glob
from shutil import copy
from pathlib import PurePath
from os.path import normpath, basename


def im_cp(cw_dir, keywrd, new_dir, postfix):
    """ Copies a given image or all images in the working directory to a given
    directory with a given keyword added in the bane of each image
    Parameters
    ---------
    cw_dir: str or list
        The full path of the imageimages or the folder containing image(s).
    keywrd: string
        Looks for all files that have this keyword in their name. If none
        provided then it looks for all .nii and .nii.gz files.
    new_dir: str
        Full path of destination folder. If none copies in cwd with postfix.
    postfix: str
        The word that is added in the end of image name
    """
    
    # Check the parameteres 
    if not cw_dir:
        cw_dir = os.getcwd()
    if not new_dir:
        new_dir = cw_dir
        if keywrd is None:
            keywrd = '*.nii*'
    # if following also is true, then there is no point
            if postfix is None:
                print('missing search keyword and/or postfix')
    
    # deal with slashes
    destin_dir = os.fspath(PurePath(new_dir))
    source_dir = os.fspath(PurePath(cw_dir))
    
    # create the search path for glob
    glob_path = source_dir + keywrd
    img_list = sorted(glob.glob(glob_path))
    
    # go through the list
    for 
    #TODO: go through subjects and apply mv
    
