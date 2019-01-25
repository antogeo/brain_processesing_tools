% Load spm_check_reg() for a list of subjects in the "subjects" folder.
% folders structure: subjects -> subject1, subject2, subject3 ... ->
% -> niftis including keywords (line 25)
% - Chose via the first GUI the folder containing the subjects ()
% - chose via the GUI the template you want to use
% - change subject by clicking enter in the command window
% antogeo 2018

% clear memory and command line (comment out if not needed)
clear; clc;
[~,pc_name]= system('hostname');
if regexp(string(pc_name), 'comameth')
    cur_path = '/home/coma_meth/Documents/PET/pet_suv_db/Liege/subjects';
elseif regexp(pc_name, 'antogeo-XPS')
    cur_path = '/home/antogeo/data/PET/pet_suv_db/Paris/subjects';
elseif regexp(pc_name, 'antogeo')
    cur_path = 'home/antogeo/Documents/';
end

folder_name = uigetdir(cur_path);
[tmplt, path] = uigetfile({'.nii'}, '~/Dropbox/current_work/fixed');
subj_name = dir(folder_name);
for i = 3: size(subj_name, 1)
    files = dir(fullfile(folder_name, subj_name(i).name));
    % look for files containing keyword
    subjs_2check = files(contains({files.name}, [ "s8SUV.nii", "s8RAW.nii" , ...
        "wSUV", "wRAW"]));
    img_2show = {};
    for num = 1: size(subjs_2check, 1)
        img_2show = [img_2show; fullfile(folder_name, subj_name(i).name, char(subjs_2check(num).name))];
    end
    if ~isempty(img_2show)
        input('Press ''Enter'' to continue...','s');
        fprintf("Subject #%d \n", i-2);
        spm_check_registration( ...
            fullfile(path, tmplt),  ...
            img_2show{:})
    end
end
