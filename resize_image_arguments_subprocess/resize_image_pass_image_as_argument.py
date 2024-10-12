#to run the code:
#python .\resize_image_pass_image_as_argument.py --image_path 40044.png


import cv2 
import os 
from argparse import ArgumentParser

def main(args):
    image_name = args.image_path
    img = cv2.imread(image_name)
    resized = cv2.resize(img, (256, 256))
    cv2.imwrite("resized_"+image_name, resized)
    

if __name__ == "__main__":
    parser = ArgumentParser(description="resize images")
    parser.add_argument("--image_path", type=str, default='40045.png' , help="path to the image")
    args = parser.parse_args()
    main(args)