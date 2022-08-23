import json
import boto3

print('Loading function')

def lambda_handler(event, context):
	print('------------------------')
	print(event)
	#1. Iteracion sobre cada registro
	try:
		for record in event['Records']:
			#2. Manejo de tipo de evento
			if record['eventName'] == 'INSERT':
				handle_insert(record)
			elif record['eventName'] == 'MODIFY':
				handle_modify(record)
			elif record['eventName'] == 'REMOVE':
				handle_remove(record)
		print('------------------------')
		return "Success!"
	except Exception as e: 
		print(e)
		print('------------------------')
		return "Error"


def handle_insert(record):
	print("Handling INSERT Event")
	
def handle_modify(record):
    print("Handling MODIFY Event")
    #3. Envio de notificion
    notification = "Esta es una notificacion de que han visitado tu pagina web."
    client = boto3.client('sns')
    response = client.publish (
        TargetArn = "arn:aws:sns:us-east-1:{YOUR_ACCOUNT_ID}:AlertasVisitaWeb",
        Message = json.dumps({'default': notification}),
        MessageStructure = 'json')
    print("Se proceso el evento DDBStream de modifiacion y notificacion enviada via email y sms")
    return {'statusCode': 200,
            'body': json.dumps(response)}

def handle_remove(record):
	print("Handling REMOVE Event")

