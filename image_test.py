## test file to see if i can display images in terminal

from PIL import Image

image_loc = '/gws/nopw/j04/dcmex/users/ezriab/image_labelling/test_random_sample/1749002_23ch1.png'
img = Image.open(image_loc)
img.show() 