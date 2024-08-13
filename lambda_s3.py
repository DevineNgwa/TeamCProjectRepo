import json
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
BUCKET_NAME = 'teamcbucket'  # Replace with your actual bucket name

def lambda_handler(event, context):
    http_method = event['httpMethod']
    path = event['path']
    
    if path == '/bucket':
        if http_method == 'GET':
            return get_object(event)
        elif http_method == 'PUT':
            return put_object(event)
        elif http_method == 'DELETE':
            return delete_object(event)
        elif http_method == 'POST':
            return list_objects(event)
    
    return {
        'statusCode': 400,
        'body': json.dumps('Invalid path or method')
    }


def get_object(event):
    key = event['queryStringParameters']['key']
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
        content = response['Body'].read().decode('utf-8')
        return {
            'statusCode': 200,
            'body': json.dumps(content)
        }
    except ClientError as e:
        return {
            'statusCode': 404,
            'body': json.dumps(f"Object not found: {str(e)}")
        }

def put_object(event):
    key = event['queryStringParameters']['key']
    content = json.loads(event['body'])
    try:
        s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=json.dumps(content))
        return {
            'statusCode': 200,
            'body': json.dumps(f"Object {key} uploaded successfully")
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error uploading object: {str(e)}")
        }

def delete_object(event):
    key = event['queryStringParameters']['key']
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=key)
        return {
            'statusCode': 200,
            'body': json.dumps(f"Object {key} deleted successfully")
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error deleting object: {str(e)}")
        }



def list_objects(event):
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        objects = [obj['Key'] for obj in response.get('Contents', [])]
        return {
            'statusCode': 200,
            'body': json.dumps(objects)
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error listing objects: {str(e)}")
        }