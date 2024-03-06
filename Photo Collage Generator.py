from PIL import Image
import os

def create_photo_sheet(input_photos, output_sheet, sheet_size=(1800, 1200), photo_size=(425, 575), rows=2, columns=4):
    sheet = Image.new('RGB', sheet_size, (255, 255, 255))
    margin_x = (sheet_size[0] - columns * photo_size[0]) // (columns + 1)
    margin_y = (sheet_size[1] - rows * photo_size[1]) // (rows + 1)

    x, y = margin_x, margin_y

    for photo_path in input_photos:
        photo = Image.open(photo_path)
        photo = photo.resize(photo_size, Image.ANTIALIAS)
        sheet.paste(photo, (x, y))

        x += photo_size[0] + margin_x

        if x + photo_size[0] + margin_x > sheet_size[0]:
            x = margin_x
            y += photo_size[1] + margin_y

    sheet.save(output_sheet)

def convert_photos_to_sheets(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            # Read the image
            input_path = os.path.join(input_folder, filename)

            # Create the output sheet path
            output_sheet = os.path.join(output_folder, os.path.splitext(filename)[0] + '_sheet.jpg')

            # Convert and save the image to the output folder as a sheet
            create_photo_sheet([input_path] * 8, output_sheet)

    print("Conversion completed.")

# Example usage
input_photo_folder = '/content/Photos'  # Replace with the actual path to your input photo folder
output_sheet_folder = '/content/Output'  # Replace with the desired output folder

convert_photos_to_sheets(input_photo_folder, output_sheet_folder)