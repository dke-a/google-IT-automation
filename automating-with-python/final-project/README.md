# Automate Updating Catalog Information

**Objective:**
Develop an automated system to update the online catalog of a fruit store with new product data provided by suppliers.


1. **Image and Description Processing:**
    - Receive product data in two file formats: .TIF (images) and .txt (descriptions).
    - Convert .TIF images to smaller, web-optimized JPEG format.
    - Transform text descriptions into HTML files, incorporating the corresponding JPEG images.
2. **Catalog Update Automation:**
    - Develop a Python script to automate the processing of images and descriptions.
    - Upload the contents of the HTML files to the company's online website using a Django-based web service.
3. **Data Extraction and Upload:**
    - Extract the name and weight of each fruit from the .txt files.
    - Use a Python request to upload this data to the Django server.
4. **Supplier Notification:**
    - On completion of the upload process, send an email to the supplier.
    - The email should include the total weight of the fruit uploaded and have a PDF attachment listing the name and total weight of each fruit.
5. **PDF Generation:**
    - Automatically generate a PDF document with the name and total weight of the uploaded fruits.
6. **System Health Check:**
    - Implement a script to monitor the health status of the system.
    - Automatically send an email notification if any issues are detected.

**Deliverables:**

1. Python scripts for image and description processing, and for updating the online catalog.

- [`changeImage.py`](./changeImage.py): Processes images and modifies according to specification.
  - Meets task 1 requirements.
- [`run.py`](./run.py): Processes and uploads product descriptions to web server. [`supplier_image_upload.py`](./supplier_image_upload.py): Uploads images to server.
  - Meets task 2 and 3 requirements.

2. Email notification system to suppliers with PDF attachment.

- [`emails.py`](./emails.py): Defines functions for sending emails.
- [`report_email.py`](./report_email.py): Processes txt files, generates a pdf report and sends an email.
  - Meets task 4 and 5 requirements.

3. System health monitoring script with alerting functionality.

- [`health_check.py`](./health_check.py): Monitors server metrics and sends an alert via email if thresholds are triggered.

