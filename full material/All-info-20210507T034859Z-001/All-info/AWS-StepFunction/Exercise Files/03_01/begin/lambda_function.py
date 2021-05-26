# in the function folder and within Cloud9
# install the package with:
# sudo pip install --target=.  pyzipcodeapi

import sys
import json
sys.path.append("ZipCodeDistance/")
from pyzipcodeapi.api import ZipCodeApi

# This function calculates the distance between two U.S. Zip Codes
def lambda_handler(event, context):
    
    print(context)
    print(event)
    
    # API Key
    # get yours at https://www.zipcodeapi.com/
    obj=ZipCodeApi("YWiVicG52p7Vaaco0Fim6zTmDFvgCK0zEmzZRONXPZcqYJg94pJhnLsWXjT2R3sJ")
    f = 'json'
    u = 'mile'
    warehouse_zip=event["Closest_WareHouse_Zip"]
    dest_zip=event["Destination_Zip"]
    
    return {
        'statusCode' : 200,
        'body': obj.get('distance', f).filter(zip_code1=warehouse_zip, zip_code2=dest_zip, units=u)
    }