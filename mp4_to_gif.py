import os 
from moviepy.editor import VideoFileClip

def mp4_to_gif(input_file, output_file):
    clip =  VideoFileClip(input_file)
    clip.write_gif(output_file)


if __name__ == "__main__":

    directory_path = './results_sgan_faces/'
    mp4_files = [file for file in os.listdir(directory_path) if file.endswith(".mp4")]

    output_dir = directory_path+'gif/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    
    
    for file in mp4_files:
        
        file_name, _ = os.path.splitext(file)
        final_file_name = file_name +'.gif'
        
        #mp4_to_gif('./results_sgan_faces/2024_10_24_17.46.33.mp4', "./results_sgan_faces/gif/output_image.gif")
        mp4_to_gif(directory_path+file, output_dir+final_file_name)
        