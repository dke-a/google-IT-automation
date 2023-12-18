#!/usr/bin/env python3
import os
import reports
import emails
from datetime import datetime

def get_fruits(description_dir):
    """Processes directory of txt files into a dictionary."""
    all_fruits = []
    for file_name in os.listdir(description_dir):
        if file_name.endswith('.txt'):
            file_path = os.path.join(description_dir, file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                fruit_items = {
                "name": lines[0].strip(),
                "weight": lines[1].strip(),
                }
                all_fruits.append(fruit_items)
    return all_fruits

if __name__ == '__main__':
    # Example usage

    current_dir = os.path.abspath(os.path.curdir)
    description_dir = current_dir+'/supplier-data/descriptions'

    today = datetime.now().strftime("%B %d, %Y")
    title = f"Processed Update on {today}"

    paragraph = get_fruits(description_dir)
    reports.generate_report("processed.pdf", title, paragraph)

    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."  # Convert summary to a single string with '\n' for line breaks
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"

    message = emails.generate(sender, receiver, subject, email_body, current_dir+"/processed.pdf")
    # Send Email
    emails.send(message)


#####

# First version of get_fruits function.
# Reads files and extracts needed data into a string.

# def get_fruits(description_dir):
#     fruit_items = ''
#     for file_name in os.listdir(description_dir):
#         if file_name.endswith('.txt'):
#             file_path = os.path.join(description_dir, file_name)
#             with open(file_path, 'r') as file:
#                 lines = file.readlines()
#                 fruit_items += f"name: {lines[0].strip()}<br/>weight: {lines[1].strip()}<br/><br/>"
#     return fruit_items