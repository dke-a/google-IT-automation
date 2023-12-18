#!/usr/bin/env python3

import psutil
import socket
import time
import emails
import os

def check_cpu_usage():
    return psutil.cpu_percent(1) > 80

def check_disk_space():
    du = psutil.disk_usage('/')
    return du.percent > 80  # Less than 20% space means over 80% is used

def check_memory():
    available = psutil.virtual_memory().available
    return available / (1024 * 1024) < 500  # Convert to MB

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != '127.0.0.1'

def send_alert(subject):
    email = emails.generate_error_report("automation@example.com", "{}@example.com".format(os.environ.get('USER')), subject, "Please check your system and resolve the issue as soon as possible.")
    emails.send(email)

while True:
    if check_cpu_usage():
        send_alert("Error - CPU usage is over 80%")
    if check_disk_space():
        send_alert("Error - Available disk space is less than 20%")
    if check_memory():
        send_alert("Error - Available memory is less than 500MB")
    if check_localhost():
        send_alert("Error - localhost cannot be resolved to 127.0.0.1")

    time.sleep(60)  # Check every 60 seconds
