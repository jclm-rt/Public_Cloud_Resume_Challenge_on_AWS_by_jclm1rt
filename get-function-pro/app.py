import json
import boto3


def lambda_handler(event, context):
    
    #1.- Log the event
    print('*********** The event for get function is: ***************')
    print(event)
    
    #2.-  Getting number of visits
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge-jclm1rt-pro')
    response = table.get_item(Key={"ID": "visitas"})
    responseBody = int(response['Item']['cantidad'])
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "https://resume.juliocesarlapaca.com",
                    "Access-Control-Allow-Methods": "*",
                    "Access-Control-Allow-Headers": "*"},
        "body": json.dumps({
            "count": responseBody
        }),
    }


    #try:
    #    ip = requests.get("http://checkip.amazonaws.com/")
    #except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
    #    print(e)

    #    raise e
