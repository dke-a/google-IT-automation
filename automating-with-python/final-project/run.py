#! /usr/bin/env python3

import os
import requests
import json


current_dir = os.path.abspath(os.path.curdir)
description_dir = current_dir+'/supplier-data/descriptions'

def process_description(file_path,file_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        description = {
            "name": lines[0].strip(),
            "weight": lines[1].replace('lbs','').strip(),
            "description": lines[2].strip(),
            "image_name": file_name.replace('.txt','.jpeg')
        }
        return description
    
# List all .txt files

if __name__ == '__main__':
    for file_name in os.listdir(description_dir):
        if file_name.endswith('.txt'):
            file_path = os.path.join(description_dir, file_name)
            description_data = process_description(file_path,file_name)
            print(description_data)

            # URL to POST the data
            response = requests.post('http://34.23.72.200/fruits/', json=description_data)

            # Check if the POST request was successful
            if response.status_code == 201:
                print(f"Description from {file_name} uploaded successfully.")
            else:
                print(f"Failed to upload {file_name}. Status code: {response.status_code}, Response: {response.text}")