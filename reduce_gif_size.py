import os 

from moviepy.editor import VideoFileClip

def reduce_gif_size(input_path, output_path, fps, resize_factor):

    # Load the video or GIF file
    clip = VideoFileClip(input_path)
    
    # Adjust the frame rate (fps) and resize the resolution
    clip = clip.set_fps(fps).resize(resize_factor)
    
    # Write the output GIF
    clip.write_gif(output_path, program='ffmpeg')
    print(f"Reduced GIF saved to {output_path}")


if __name__ == "__main__":
    directory_path = './results_sgan/gif/'
    mp4_files = [file for file in os.listdir(directory_path) if file.endswith(".gif")]

    output_dir = directory_path+'reduced/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    
    for file in mp4_files:
        
        #mp4_to_gif('./results_sgan_faces/2024_10_24_17.46.33.mp4', "./results_sgan_faces/gif/output_image.gif")
        #mp4_to_gif(directory_path+file, output_dir+final_file_name)
        

        # # Example usage
        # input_gif = "./results_sgan/gif/2024_10_24_12.11.25.gif"  # Or .gif if you're starting with a GIF
        # output_gif = "./results_sgan/gif/2024_10_24_12.11.25_reduced.gif"
        # reduce_gif_size(input_gif, output_gif, fps=8, resize_factor=0.5)

                # Example usage
        input_gif = directory_path+file #"./results_sgan/gif/2024_10_24_12.11.25.gif"  # Or .gif if you're starting with a GIF
        output_gif = output_dir+file#"./results_sgan/gif/2024_10_24_12.11.25_reduced.gif"
        reduce_gif_size(input_gif, output_gif, fps=10, resize_factor=0.8)

