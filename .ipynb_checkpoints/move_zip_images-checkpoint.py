## quick script to move images into a folder, based on a label so i can view them
# also zips up the folder

import numpy as np
import pandas as pd
import os
import shutil

folder_path = '/gws/nopw/j04/dcmex/users/ezriab/image_labelling/2ds_10000_sample/'
csv_file_name = '2ds_10000_new.csv'
csv_read_pd = pd.read_csv(folder_path+csv_file_name)

category_dic = {'1.0':'CP','2.0':'FA','3.0':'Co','4.0':'HPC','6.0':'CBC','7.0':'CA','8.0':'CC','9.0':'WD','0.0':'DIF','11.0':'unknown'}
category_dic_extra = {} # adding in path to loc 
for key in category_dic:
    var_name = category_dic[key]
    individ_cat_path = folder_path+var_name+'/'
    category_dic_extra[key] = [var_name,individ_cat_path]

length_of_data = len(csv_read_pd['image_name'])
for idx in range(length_of_data):
    row = csv_read_pd.loc[idx]
    image_name = row.iloc[0]
    label = row.iloc[1]
    og_loc = folder_path+image_name+'.png'
    new_loc = category_dic_extra[str(label)][1]
    
    shutil.copy(og_loc, new_loc)

print('copying images finished')

# zip up the folders with images in
for key in category_dic_extra:
    cat_folder = category_dic_extra[key][0]
    folder_path_to_zip = category_dic_extra[key][1][:-1]
    shutil.make_archive(folder_path_to_zip, 'zip',folder_path_to_zip) # as we are saving with same name but with .zip
    print(f'{cat_folder} zipped!')