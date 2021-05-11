import json
def handler(event, context):    
    return {"message": "Successfully executed"}

def add_user():
    data = {"a":"abcd"}
    datastr = json.d