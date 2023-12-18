#!/usr/bin/env python3

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, fruits_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment, pagesize=letter)
    report_title = Paragraph(title, styles["h1"])
    content = [report_title, Spacer(1, 20)]

    for fruit in fruits_data:
        name_paragraph = Paragraph(f"name: {fruit['name']}", styles["BodyText"])
        weight_paragraph = Paragraph(f"weight: {fruit['weight']}", styles["BodyText"])
        content.extend([name_paragraph, weight_paragraph, Spacer(1, 20)])

    report.build(content)


####

# def generate_report(attachment, title, paragraph):
    """Creates standard report with string formatted paragraph"""
#     styles = getSampleStyleSheet()
#     report = SimpleDocTemplate(attachment, pagesize=letter)
#     report_title = Paragraph(title, styles["h1"])
#     report_info = Paragraph(paragraph, styles["BodyText"])

#     empty_line = Spacer(1, 20)

#     content = [report_title, empty_line, report_info]
#     report.build(content)
