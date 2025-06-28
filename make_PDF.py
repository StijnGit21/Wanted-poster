from fpdf import FPDF
import os

folder_path = "C:\\Users\\stijn\\Pictures\\wanted poster\\output"
output_pdf_path = "C:\\Users\\stijn\\Pictures\\wanted poster\\bijlage.pdf"

def create_pdf_with_images(folder_path, output_pdf_path):
    # List all files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Create a PDF object
    pdf = FPDF()

    # Add a page for each image
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        pdf.add_page()

        # Adjust the x, y, and w parameters as needed
        x_position = 0  # Horizontal position in mm
        y_position = -15  # Vertical position in mm
        width = 210     # Width of the image in mm

        pdf.image(image_path, x=x_position, y=y_position, w=width)

    # Save the PDF to the specified path
    pdf.output(output_pdf_path, "F")

# Example usage
create_pdf_with_images(folder_path, output_pdf_path)
