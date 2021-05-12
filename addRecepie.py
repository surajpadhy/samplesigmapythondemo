import boto3
ddb = boto3.client("dynamodb")
import json

def add_recepie(event, context):
    print("EVENT: ",event)
    recepie_id = event["recepie_id"]
    recepie_name = event["recepie_name"]
    desc = event["desc"]
    try:
        recepie_response = ddb.put_item(
            TableName="Recepie",
            Item={
                'recepie_id': {"S":recepie_id},
                'recepie_name': {"S":recepie_name},
                'desc': {"S":desc}
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    return {"message":"Recepie added"}
