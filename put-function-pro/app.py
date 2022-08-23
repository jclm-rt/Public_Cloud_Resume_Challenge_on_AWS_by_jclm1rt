import json
import boto3
# import requests

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge-jclm1rt-pro')

def lambda_handler(event, context):
    key={
        'ID':'visitas'
    }
    dbresponse = table.get_item(Key=key)
    item=dbresponse['Item']
    print(item)
    record_count = dbresponse['Item']['cantidad']
    record_count = record_count + 1
    item = {
        'ID':'visitas',
        'cantidad': record_count
    }
    dbresponse = table.put_item(Item=item)
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "https://resume.juliocesarlapaca.com",
                    "Access-Control-Allow-Methods": "*",
                    "Access-Control-Allow-Headers": "*",
                    "authorizationToken": "abc123"},
        "body": "cantidad de visitantes incrementada correctamente"
    }


# client = boto3.client('secretsmanager')
# response = client.get_secret_value(
#     SecretId='prod/slack/webhook'
# )
# database_secrets = json.loads(response['SecretString'])
# webhook_url = database_secrets['password']
# data = {
#     "text": "esta es una prueba de texto para webhook de slack"
# }
# headers = {'Content-Type': 'application/json'}
# response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

