#!/usr/bin/env python3

import requests
import os

path = "/home/student-00-2ba060bb2a28/supplier-data/images/"
url = "http://localhost/upload/"
files = os.listdir("/home/student-00-2ba060bb2a28/supplier-data/images/")

for img in files:
        if img.endswith(".jpeg"):
                with open(path+img, 'rb') as opened:
                        r = requests.post(url, files={'file': opened})
