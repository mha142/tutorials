import os
import subprocess 


original_image_path = './'

for image_name in os.listdir(original_image_path):
    if image_name.endswith('.png'):
        print(image_name)
        subprocess.run(['python', 'resize_image_pass_image_as_argument.py', '--image_path', image_name]) #'40044.png'

