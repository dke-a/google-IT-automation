from PIL import Image
import os

current_dir = os.path.abspath(os.path.curdir)
input_folder = current_dir+"/m1-images"
output_folder = current_dir+"/icons"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if os.path.isfile(file_path):
        print(file_path,"\n")
        try:
            with Image.open(file_path) as img:
                img = img.convert('RGB').rotate(-90, expand=True).resize((128, 128))
                output_path = os.path.join(output_folder, filename + '.jpeg')
                img.save(output_path)
        except IOError:
            print(f"Cannot process file {filename}")

print("Processing complete.")
