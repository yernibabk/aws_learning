
import json
import time
import random

# This function calculates volume based on dimensions
def lambda_handler(event, context):
   # print
  
   #print (event)
    
   # gather values from the input document
   length=event["Input"]["Volume"]["length"]
   width=event["Input"]["Volume"]["width"]
   height=event["Input"]["Volume"]["height"]
   
   # calculate
   vol = length * width * height
    
   a = 5
   b = 0
   
   # Simulate a crash dividing by zero
   if random.random() > 0.9:
     c = a / b
    
   # Simulate a timeout randomly, half the time
   if random.random() > 0.5:
     time.sleep(5)
    
   return {
        'Package Volume' : vol
    }