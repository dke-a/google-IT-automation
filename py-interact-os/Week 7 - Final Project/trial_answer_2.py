import re
import csv

# Initialize dictionaries
error_dict = {}
user_dict = {}

# Regular expressions for matching log entries
info_pattern = r"INFO (.*) \((.*)\)" #could do without username regex
error_pattern = r"ERROR (.*) \((.*)\)"

current_dir = os.path.abspath(os.path.curdir) # make sure running from script directory
description_dir = current_dir+'/syslog.log'

# Iterate over log entries in syslog.log
with open(description_dir) as file:
    for line in file:
        # Match INFO log entries
        match = re.search(info_pattern, line)
        if match:
            #print(match.group(2))
            #info_message = match.group(1)
            #username = re.search(r"\((.*)\)", info_message).group(1)
            username = match.group(2)
            if username not in user_dict:
                user_dict[username] = {'INFO': 0, 'ERROR': 0}
            user_dict[username]['INFO'] += 1

        # Match ERROR log entries
        match = re.search(error_pattern, line)
        if match:
            
            error_message = match.group(1)
            username = match.group(2)
            if username not in user_dict:
                user_dict[username] = {'INFO': 0, 'ERROR': 0}
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
