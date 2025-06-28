from PIL import Image, ImageOps
import os

# Constants for positions, sizes, and paths
PHOTO_POSITION = (90, 230)
PHOTO_SIZE = (280, 280)
TEMPLATE_PATH = "C:\\Users\\stijn\\Pictures\\wanted poster\\poster.jpg"
PHOTO_FOLDER = "C:\\Users\\stijn\\Pictures\\wanted poster\\input"
OUTPUT_FOLDER = "C:\\Users\\stijn\\Pictures\\wanted poster\\output"

def create_wanted_poster(template_path, photo_path, output_path):
    template = Image.open(template_path)
    photo = Image.open(photo_path)

    # Correct the orientation of the photo based on EXIF data
    photo = ImageOps.exif_transpose(photo)

    # Resize the photo to fit the template
    photo = photo.resize(PHOTO_SIZE)

    # Paste the photo onto the template at the specified position
    template.paste(photo, PHOTO_POSITION)

    # Save the result
    template.save(output_path)

def main():
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Loop through all photos in the photo folder
    for photo in os.listdir(PHOTO_FOLDER):
        if photo.lower().endswith(('.png', '.jpg', '.jpeg')):
            photo_path = os.path.join(PHOTO_FOLDER, photo)
            output_path = os.path.join(OUTPUT_FOLDER, f'wanted_{photo}')
            create_wanted_poster(TEMPLATE_PATH, photo_path, output_path)

if __name__ == "__main__":
    main()
