import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'users_db'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Extract username and age from query parameters
    userid = event.get('userid')
    username = event.get('username')
    age = event.get('age')

    # Insert data into DynamoDB
    try:
        item = {
            'userid': userid,
            'username': username,
            'age': age
        }
        table.put_item(Item=item)

        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data inserted successfully'})
        }
    except Exception as e:
        # Return an error response if insertion fails
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }