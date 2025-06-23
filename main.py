from PIL import Image
import os

# Constants for positions, sizes, and paths
PHOTO_POSITION = (50, 50)
PHOTO_SIZE = (200, 200)
TEMPLATE_PATH = 'path/to/your/template.png'
PHOTO_FOLDER = 'path/to/your/photos'
OUTPUT_FOLDER = 'path/to/your/output'

def create_wanted_poster(template_path, photo_path, output_path):
    template = Image.open(template_path)
    photo = Image.open(photo_path)

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
