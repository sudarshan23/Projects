i#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, para):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    report_info = Paragraph(para, styles["BodyText"])
    report.build([report_title,empty_line, report_info])
