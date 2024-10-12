import cv2 
import os 


#original_path = "./real_images_1200_1024x1024/picked_real_images_1200/"
#original_path = "./real_images_1200_1024x1024/picked_real_1200_face_only/"
#original_path = "./stylegan2_600_1024x1024/picked_stylegan2_600/"
original_path = "./stylegan2_600_1024x1024/picked_stylegan2_600_face_only/"


#go through all the images in the folder 
count = 0
for image_name in os.listdir(original_path):

    img = cv2.imread(original_path+image_name)

    resized = cv2.resize(img, (256, 256))

    #result_path = "./real_images_1200_256x256/"
    #result_path = "./real_images_1200_256x256_face_only/"
    #result_path = "./stylegan2_images_1200_256x256/"
    result_path = "./stylegan2_images_1200_256x256_face_only/"

    cv2.imwrite(result_path+"resized_"+image_name, resized)