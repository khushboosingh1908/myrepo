import json
import boto3

client = boto3.client('dynamodb')

def handler(event, context):
  data = client.get_item(
    TableName='MyWebTable',
    Key={
        'id': {
          'a': '005'
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response
