# Sample list of URLs for the images

# try to read from a txt file
with open('./images_arrays/sgan_images_links.txt', 'r') as file:
    #lines = file.read()
    lines = file.readlines()
    
    #for line in lines:
    image_dict = {f"s{i+1}": url for i, url in enumerate(lines)}

    for key, value in image_dict.items():
        value = value.rstrip('\n') #take away the new line character that exist at the end of each line 
        print(f"'{key}': '{value}',")

