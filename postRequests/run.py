#! /usr/bin/env python3

import os
import requests

#for r,d,f in os.walk('/data/feedback'):
  #continue

'''
Assignment to perform data  serialization in Python using requests module
'''

source = "/data/feedback/"
feedbackFile=os.listdir(source)

feedbacks=[]
i=0

for feedback in feedbackFile:
  with open(source+feedback, 'r') as file:
    feedbacks.append({})
    feedbacks[i]['id']= i+1
    feedbacks[i]['title']= file.readline().strip()
    feedbacks[i]['name']= file.readline().strip()
    feedbacks[i]['date']= file.readline().strip()
    feedbacks[i]['feedback']= file.readline().strip()
  i+=1

url='http://35.225.115.205/feedback/'
for item in feedbacks:
  response = requests.post(url,data=item)
  print(response.status_code)
