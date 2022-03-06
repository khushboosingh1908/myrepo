import requests
import json

def lambda_handler(event, context):
    url = "http://dummy.restapiexample.com/api/v1/employee/"+str(event['id'])
    response = requests.get(url=url)
    response_body = json.loads(response.text)
    return process_response(response.status_code, response_body)    
        
def process_response(status_code, body):
    return {
        'statusCode': status_code,
        'body': body
    }
