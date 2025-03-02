import os
from PIL import Image

# Function to resize and fit the logos into the transparent canvas
def fit_logos_to_canvas(input_folder, output_folder, canvas_width=400, canvas_height=173):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):  # Process only PNG files
            file_path = os.path.join(input_folder, filename)
            try:
                # Open the logo image
                img = Image.open(file_path)
                
                # Handle images with transparency issues by converting to 'RGBA' mode
                if img.mode != 'RGBA' and img.mode != 'RGB':
                    img = img.convert('RGBA')
                
                # Resize the logo to fit within the 400x173 canvas while maintaining aspect ratio
                img.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

                # Create a new transparent canvas of size (400x173)
                canvas = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))

                # Calculate the position to paste the resized logo onto the center of the canvas
                logo_width, logo_height = img.size
                x_position = (canvas_width - logo_width) // 2
                y_position = (canvas_height - logo_height) // 2

                # Paste the resized logo onto the canvas
                canvas.paste(img, (x_position, y_position), img)  # Use img as a mask for transparency

                # Save the new image to the output folder
                output_path = os.path.join(output_folder, filename)
                canvas.save(output_path, 'PNG')
                print(f"Saved: {output_path}")
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
input_folder = 'techlogo'  # Folder containing the original PNG logos
output_folder = 'techlogo_resized'  # Folder where resized logos will be saved

fit_logos_to_canvas(input_folder, output_folder)
