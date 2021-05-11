import boto3
ddb = boto3.client("dynamodb")
import json

def handler(event, context):    
    return {"message": "Successfully executed"}

def add_user(event, context):
    data = {"a":"abcd"}
    datastr = json.dumps(data)
    print(datastr)

    try:
        recepie = ddb.get_item(
            TableName="Recepie",
            Key={
                'recepie_id': {
                    'S': recepie_id
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    return {"message":"Retrieved Recepie", "recepie":recepie}
    

