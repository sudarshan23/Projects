#!/usr/bin/env python3

import os
from datetime import date
import reports
import json
import emails

def main():
        with open("json_file","r") as json_d:
                data=json.load(json_d)

        paragraph=''
        for record in data:
                paragraph += "name: " + record['name'] + "<br/>" +"weight: "+ str(record['weight']) + " lbs<br/><br/>"


        attachment="/tmp/processed.pdf"
        title = "Processed Update on " + str(date.today().strftime("%B %d, %Y"))
        reports.generate_report(attachment, title, paragraph)
        SENDER = "automation@example.com"
        TO="student-00-2ba060bb2a28@example.com"
        SUBJECT="Upload Completed - Online Fruit Store"
        BODY="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
        ATTACH="/tmp/processed.pdf"
        emails.send_email(emails.generate_email(SENDER,TO,SUBJECT,BODY,ATTACH))


if __name__ == "__main__":
        main()
