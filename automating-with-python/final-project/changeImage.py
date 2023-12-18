#!/usr/bin/env python3

from PIL import Image
import os

current_dir = os.path.abspath(os.path.curdir)
input_folder = current_dir+"/supplier-data/images"
output_folder = current_dir+"/supplier-data/images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.tiff'):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    img = img.convert('RGB').resize((600, 400))
                    filename = filename.replace('.tiff','.jpeg')
                    output_path = os.path.join(output_folder, filename)
                    img.save(output_path)
                    print(file_path,"\n")
                    print(img.format,img.size,"\n")
            except IOError:
                print(f"Cannot process file {filename}")

print("Processing complete.")

