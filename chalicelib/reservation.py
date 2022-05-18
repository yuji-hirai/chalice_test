from chalicelib.lambda_layer import week_day
import requests
import boto3

dynamo_client = boto3.client('dynamodb')

TABLE_NAME = 'Thread'

request_url = "https://qiita.com/"
requests_get = requests.get(request_url)
status_code = requests_get.status_code

def dispatch(user_phone):
  response = dynamo_client.Table("testdb").get_item(Key={
  'user_phone': user_phone
  })
  return response