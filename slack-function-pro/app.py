import json
import boto3
import requests
import base64
from botocore.exceptions import ClientError



def get_secret_slack_notification():

    secret_name = "prod/slack/webhook"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
        slack_secrets = json.loads(secret)
    else:
        decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
        
    webhook_url = slack_secrets["SLACK_WEBHOOK_URL"]
    print(webhook_url)
    data = {
        "text": "Tu website serverless ha sido visitado"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

#get_secret_slack_notification()

def lambda_handler(event, context):
    print("invocando funcion de slack")
    get_secret_slack_notification()
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "https://resume.juliocesarlapaca.com",
                    "Access-Control-Allow-Methods": "*",
                    "Access-Control-Allow-Headers": "*"},
        "body": "mensaje enviado a slack"
    }






