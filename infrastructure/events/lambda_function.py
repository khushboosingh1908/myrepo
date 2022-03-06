import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyWebTable')

def lambda_handler(event, context):
  itemid = event['queryStringParameter']['itemid']
  
  result = table.get_item(Key={'itemId': itemid})

  response = {
      'statusCode': 200,
      'body': json.dumps(response)
  }
  
  return response
