import re
import csv

# Initialize dictionaries
error_dict = {}
user_dict = {}

# Regular expressions for matching log entries
info_pattern = r"INFO (.*)"
error_pattern = r"ERROR (.*) \((.*)\)"
username_pattern = r"\((.*)\)"

# Iterate over log entries in syslog.log
with open('/Users/don/Documents/Python Scripts/Coursera - Google IT/py-interact-os/Week 7 - Final Project/syslog.log') as file:
    for line in file:
        
        match_info = re.search(info_pattern, line)
        match_error = re.search(error_pattern, line)
        
        if match_info or match_error:
            match_username = re.search(username_pattern,line)
            username = match_username.group(1)
            if username not in user_dict:
                user_dict[username] = {'INFO': 0, 'ERROR': 0}

            if match_info:
                user_dict[username]['INFO'] += 1

            if match_error:
                error_message = match_error.group(1)
                user_dict[username]['ERROR'] += 1
                if error_message not in error_dict:
                    error_dict[error_message] = 0
                error_dict[error_message] += 1

               

# Sort dictionaries
sorted_error_dict = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
sorted_user_dict = sorted(user_dict.items())

# Create error_message.csv
with open('error_message.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Error', 'Count'])
    writer.writerows(sorted_error_dict)

# Create user_statistics.csv
with open('user_statistics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    for username, counts in sorted_user_dict:
        writer.writerow([username, counts['INFO'], counts['ERROR']])
