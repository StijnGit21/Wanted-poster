from PIL import Image, ImageDraw, ImageFont
import os
import random

# define paths for the template, photo folder, and output folder
template_path = 'path/to/your/template.png'
photo_folder = 'path/to/your/photos'
output_folder = 'path/to/your/output'


# Position where the photo will be placed on the template
position_picture = (50, 50)  # Adjust position as needed

# Position where the text will be placed on the template
text_position = (50, 250)  # Adjust position as needed


picture_size = (400, 600)  # Size of the wanted poster template


def create_wanted_poster(template_path, photo_path, output_path, position_picture, text_position):
    template = Image.open(template_path)
    photo = Image.open(photo_path)

    # Resize the photo to fit the template
    photo = photo.resize((picture_size))  # Adjust size as needed

    # Paste the photo onto the template at the specified position
    template.paste(photo, position_picture)

    # Extract the name from the photo filename (without extension)
    photo_name = os.path.splitext(os.path.basename(photo_path))[0]

    # Generate a random award amount
    award = random.randint(1000, 10000)

    # Use a basic font
    font = ImageFont.load_default()

    # Draw the name and award on the template
    draw = ImageDraw.Draw(template)
    draw.text(text_position, f"Name: {photo_name}", font=font, fill="black")
    draw.text((text_position[0], text_position[1] + 20), f"Award: ${award}", font=font, fill="black")

    # Save the result
    template.save(output_path)

def main():


    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all photos in the photo folder
    for photo in os.listdir(photo_folder):
        if photo.lower().endswith(('.png', '.jpg', '.jpeg')):
            photo_path = os.path.join(photo_folder, photo)
            output_path = os.path.join(output_folder, f'wanted_{photo}')
            create_wanted_poster(template_path, photo_path, output_path, position_picture, text_position)

if __name__ == "__main__":
    main()
