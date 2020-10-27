#! /usr/bin/env python3

import os
import requests
import json

url = "http://34.122.192.45/fruits"

path = "/home/student-00-2ba060bb2a28/supplier-data/descriptions/"

descrip=[]

i=0

files = os.listdir("/home/student-00-2ba060bb2a28/supplier-data/descriptions/")

for file in files:
        if file.endswith(".txt"):

                with open(path+file, 'r') as f:
                        descrip.append({})
                        descrip[i]['name']=f.readline().strip()
                        descrip[i]['weight']=int(f.readline().strip().split(' ')[0])
                        descrip[i]['description']=f.readline().strip()
                        descrip[i]['image_name']=os.path.splitext(file)[0].strip()+".jpeg".strip()
                i+=1


j_object = json.dumps(descrip)

with open("json_file","w") as j_file:
        j_file.write(j_object)


response = requests.post(url,json=j_object)
print(response.status_code)
