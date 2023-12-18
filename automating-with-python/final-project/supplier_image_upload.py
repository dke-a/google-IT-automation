#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

current_dir = os.path.abspath(os.path.curdir)
folder = current_dir+"/supplier-data/images"

# Upload images to website.

for filename in os.listdir(folder):
    if filename.endswith('.jpeg'):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            print(file_path)
            try:
                with open(file_path,'rb') as opened:
                    r = requests.post(url, files={'file': opened})
            except IOError:
                print(f"Cannot process file {filename}")

print("Processing complete.")
