## py script to tidy up all the images that have been labelled and do a bit of archiving - zip up and place into a folder

import numpy as np
import pandas as pd
import os
from PIL import Image
from glob import glob
import csv
import matplotlib.pyplot as plt
from IPython.display import clear_output
import math
import shutil
import zipfile

base_path = '/gws/nopw/j04/dcmex/users/ezriab/image_labelling/'
original_folders = ['2ds_2000_010125','2ds_3000_030125','2ds_5000_100125']
new_folder = '2ds_10000_sample'
new_save_loc = base_path+new_folder+'/'

png_2000_pth = os.path.join(base_path, original_folders[0])
png_3000_pth = os.path.join(base_path, original_folders[1])
png_5000_pth = os.path.join(base_path, original_folders[2])

three_base_paths = [png_2000_pth+'/', png_3000_pth+'/', png_5000_pth+'/']

## loop for moving all the images in the seperate folders
for main_path in three_base_paths:
    list_of_all_images = glob(main_path+'*.png')
    for image in list_of_all_images:
        shutil.copy(image, new_save_loc)


### archiving
def do_archive(directory, output_dir_name):
    shutil.make_archive(output_dir_name, 'zip', directory)

## also need to archive some things
save_archived_things = '/gws/nopw/j04/dcmex/users/ezriab/archive/'


ds_image_path = '/gws/nopw/j04/dcmex/users/ezriab/processed_images/2ds' #also 2ds  hvps in this
hvps_image_path = '/gws/nopw/j04/dcmex/users/ezriab/processed_images/hvps'
stats_path = '/gws/nopw/j04/dcmex/users/ezriab/processed_stats' ## just do whole folder


do_archive(png_2000_pth,save_archived_things+'2ds_2000_sample_010125')
print('png_2000_pth done')
do_archive(png_3000_pth,save_archived_things+'2ds_3000_sample_030125')
print('png_3000_pth done')
do_archive(png_5000_pth,save_archived_things+'2ds_5000_sample_100125')
print('png_5000_pth done')

do_archive(ds_image_path,save_archived_things+'all_2ds_processed_images')
print('2ds images done')
do_archive(hvps_image_path,save_archived_things+'all_hvps_processed_images')
print('hvps images done')
do_archive(stats_path,save_archived_things+'all_processed_stats')
print('stats done')
